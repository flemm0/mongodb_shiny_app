# Data-Driven Exploration of Racial Differences in Prostate Cancer


## Background Information

It has been known that there are racial disparities in prostate cancer incidence and mortality amongst Asian, Black, and Caucasian men. According to Hinata et al, African-American men see a 64% higher prostate cancer incidence, and a 2.3 times greater mortality rate. Furthermore, African-American men and are diagnosed at a younger age compared to Caucasian men. There has recently been an increased effort to determine the sources of the racial disparity through genomic profiling. A population-based retrospective cohort study Fairey A, Chetner M, Metcalfe J, Moore R, Todd G, Rourke K, et al, found that men of African descent were approximately twice as likely to be diagnosed with prostate cancer before the age of 45 as men of Caucasian descent.

## Objective of creating a noSQL database:

The data that I use in the project is from cBioPortal. Specifically, I used the data set published under Stopsack et al: Differences in prostate cancer genomes by self-reported race: Contributions of genetic ancestry, modifiable cancer risk factors, and clinical factors. In addition to clinical information, they provide copy number alteration, mutation, and structural variant information from each patient which was determined from a targeted sequencing panel. In their publication, the authors attempted to better understand why tumor genomes differ by self-reported race and genetic ancestry.

My objective for this project is to create a database that can store patient-level clinical and genomic data for prostate cancer patients in an easily scalable way using mongoDB. Aside from horizontal scalability, using mongoDB provides some other advantages over using the traditional relational data model in storing clinical and genomic data. Firstly, mongoDB offers a flexible schema, which handles genomic data well, which can be highly complex and varied. Additionally, the document-based format handles complex relationships between genomic and clinical information better than the traditional tabular format. Finally, if the database were to be scaled by addition of more information for each patient, or more patients, mongoDB would not see a decrease in performance, compared to SQL.


## R Shiny Application

Finally, I used R Shiny to create an interactive data visualization application to allow users to explore aspects of the data. I used the `mongolite` package from R to connect to the MongoDB backend and load data into the R environment. With the R Shiny app, uses can quickly access the data in tabular format, as well as visualize key features such as 8q arm, Age at Diagnosis, etc. with the focus being on the racial differences in some of the clinical and genomic aspects of prostate cancer.

To view the website: [click here](https://github.com/flemm0)
