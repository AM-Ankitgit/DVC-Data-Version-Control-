# this is the my demo of DVC File

<h1>https://dvc.org/doc</h1>


# How to implement the DVC
 -git log
    -- commit c10ccfde2df63457ab838786014fbe4f50
    
    File added

    -- commit 6c0a7d15b50a95847e1b64f42b12487bac65e73a



### if you want to go previous commit the Use the
   -- git checkout 86014f


# to add the data in dvc
  -- dvc add data/data.csv
  -- git commit -m "this my latest version of data"
  
  here you can add different version of data 

# if you want to retrieve specific version of data
   -- git checkout commit_id
   eg. git checkout 73782
   dvc checkout 



# to create the repository at local workspace you can keep the track of all version of data
 --dvc remote add -d <repo_name> full_path_of_repo_location_where_you_want_create
 
 eg.dvc remote add -d dvc_demp D:/study/Data_Version_Controlled(DVC)/remotestorage

  -- dvc push (you can see the latestversion of data in your workspace in remotestorage folder)

  -- git add data/data.csv.dvc
  -- git commit "Latest Version"
  -- git add .dvc/config
  -- git commit -m "Config file added"
  -- dvc push





# REPRODUCIBILITY
 - refers to the ability to achieve consistent results using the same dataset, computational methods, and analysis procedures. It ensures that experiments and their outcomes can be reliably repeated by others, including future versions of the project. Reproducibility is crucial for validating findings, building upon previous work, and fostering trust in scientific and analytical results.


## Key Aspects of Reproducibility
- Consistent Environment:
Ensuring that the computational environment (libraries, software versions, configurations) is the same as when the original analysis was performed.

- Version Control:
Using version control systems (e.g., Git) to track changes in code, data, and configurations. This helps in maintaining a history of modifications and understanding the evolution of the project.

- Data Management:
Keeping track of data versions and ensuring that the same data used in the original experiment is available for reproduction. Tools like DVC (Data Version Control) can help in managing data versions.
 

- Clear Documentation:
Providing detailed documentation of the procedures, methodologies, and parameters used in the experiment. This includes code comments, README files, and supplementary documents.

- Pipeline Automation:
Automating the workflow using tools like DVC, Make, or other workflow management systems ensures that the steps of data processing, model training, and evaluation can be executed in the same order with the same parameters.

![alt text](D:\study\Data_Version_Controlled(DVC)\images\structure_dvc_yaml.png)


## Run the pipeline:
- dvc repro  >>> generate the dvc.lock file
## Visualize the pipeline
- dvc dag (Directed acyclic graph)

