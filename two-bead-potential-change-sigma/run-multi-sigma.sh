# This is a sh script that runs

# loop over different values of h 
for h in 0.02 0.04 0.06 0.08 0.10 0.15 0.20 0.25 0.30 0.35 0.40 0.45 0.50
do
    # switch to the directory h-two digits of h
    cd h-$h
    
    # run the prepare
    # bash prepare.sh
    
    # submit jobs 
    # bash run.sh
    
    # collect energy values
    cp ../simulation-template/collect_energy.py .
    python collect_energy.py
    

    cd ..


done

