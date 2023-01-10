This project has multiple ways of documenting requirements. Since it doesn't cost anything we include them all.

- environment.yaml - This is the manual requirements, use it to install a new test or dev environment
- environment.min.yaml - This is the minimum requirements, use it to install a new test or dev environment
- environment.max.yaml - This pins all conda packages, use for production or finding vulnerabilities
- conda.requirements.txt - For people or bots not using conda

To update the files run
`bash requiresments/doc_reqs.sh`
