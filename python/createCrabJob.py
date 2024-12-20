import os
import sys
import glob
import argparse
import subprocess
import shutil
from importlib import import_module

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--sample-config', type=str, default='samples_training.py',help='python file containing list of samples')
parser.add_argument('-t', '--sample-type', nargs="+", default=[], help='list of sample type to be considered')
parser.add_argument('-c', '--crab-config', type=str, default='../crab/crabConfig_training.py',help='python file that dives the overall crabDescription')
parser.add_argument('-j', '--crab-job-dir', type=str, default='../crab/',help='directory where crab jobs folder will be created')
parser.add_argument('-m', '--command', type=str, default='submit', help="possible commands are: submit, resubmit, kill, status, getlog, erase,", choices=['submit','resubmit','kill','status','getlog','erase']);
parser.add_argument('-o', '--options', nargs="+", default=[], help="options to each specific crab command");
 
if __name__ == '__main__':

    args = parser.parse_args()

    ## import the sample config
    samples_dict = {};
    sample_module = import_module(args.sample_config.replace('.py', '').replace('/', '.'))
    if not args.sample_type or "All" in args.sample_type:
        sample_module.AddAllSamples(samples_dict);
    else:        
        if "QCD" in args.sample_type:
            sample_module.AddQCDHTSamples(samples_dict);
        elif "Top" in args.sample_type:
            sample_module.AddTopSamples(samples_dict);
        elif "VJets" in args.sample_type:
            sample_module.AddVJetsSamples(samples_dict);
        elif "ggHH4b" in args.sample_type:
            sample_module.AddGluGluHHTo4BSamples(samples_dict);
        elif "gH2b" in args.sample_type:
            sample_module.AddGluGluHToBBSamples(samples_dict);
        elif "Data" in args.sample_type:
            sample_module.AddDataSamples(samples_dict);
        else:
            sys.exit("sample type not found --> exit")
            
    # adjusting the command to submit
    if args.options:
        args.options = ["--"+s for s in args.options];

    ## loop over values and create directories or erase them                                                                                                                                          
    for key,value in samples_dict.items():    
        path = os.path.join(os.getcwd(),args.crab_job_dir,key);
        ## create directories for crab
        if (os.path.exists(path) and os.path.isdir(path)):
            print (key+" directory exists in "+os.path.join(os.getcwd(),args.crab_job_dir));
            if args.command == "erase":
                print ("Removing directory");
                shutil.rmtree(path);
        else :
            if args.command == "submit":
                print (key+" directory does not exists --> create it since command is submit");
                os.makedirs(path); 
   
    if args.command == "erase":
        sys.exit();
    else:
        mother_dir = os.getcwd();
        for key,value in samples_dict.items():    
            os.chdir(mother_dir);
            path = os.path.join(os.getcwd(),args.crab_job_dir,key);
            if not os.path.exists(path): continue;
            if not os.path.isdir(path): continue;
            if args.command == "submit":
                shutil.copy2(args.crab_config,path) 
            os.chdir(path);
            if args.command == "submit":
                crab_query = subprocess.Popen("crab submit -c "+os.path.basename(args.crab_config)+" "+" ".join(args.options),shell=True);
                crab_query.wait();
            else:
                ## other crab actions to be performed on the subfolders where the .crabcache file is located
                for dirname in os.listdir(os.getcwd()):                
                    if not os.path.isdir(dirname): continue;
                    if "__pycache__" in dirname: continue;
                    if args.command == "status":
                        print("crab status -d "+dirname+" "+" --".join(args.options))
                        crab_query = subprocess.Popen("crab status -d "+dirname+" "+" ".join(args.options),shell=True);
                        crab_query.wait();
                    elif args.command == "kill":
                        crab_query = subprocess.Popen("crab kill -d "+dirname+" "+" ".join(args.options),shell=True);
                        crab_query.wait();
                    elif args.command == "resubmit":
                        crab_query = subprocess.Popen("crab resubmit -d "+dirname+" "+" ".join(args.options),shell=True);
                        crab_query.wait();
                    elif args.command == "getlog":
                        crab_query = subprocess.Popen("crab getlog -d "+dirname+" "+" ".join(args.options),shell=True);
                        crab_query.wait();
