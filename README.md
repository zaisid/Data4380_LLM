# Countinng Shapes

* This repository holds an attempt to apply fine tuning techniques a large language model (LLM) and test/improve its ability to "count" shapes in an image.

## Overview

This project explores the use of fine-tuning techniques on a large language model (LLM) to improve its ability to perform a simple multimodal counting task: identifying and counting shapes within an image. Specifically, the model was trained and tested on synthetic image datasets containing various geometric shapes, with the goal of improving its ability to count shapes accurately from visual input. The workflow involved dataset generation, labeling with Google Cloud Vertex AI, fine-tuning a chosen LLM, and evaluating performance before and after training.



## Summary of Work Done

### Data

* Type: Image data, generated through python scripts, labelled with bounding boxes using Google Cloud and Vertex AI Studio.
* Size: approximately 350 images, each 600x600, were generated in total, though only a subset were used for training/testing (50 for training)

#### Preprocessing / Clean Up
The data required minimal processing. Python scripts were used to generate images of various types (i.e., ones with only circles, ones in grayscale, etc.), which were then uploaded and organized to a Google Cloud bucket, where they were labelled with bounding boxes.


#### Data Visualization

![Examples of given image data.](/Images/test.png)

![](/Images/test2.png)


### Problem Formation

The input would be any given image, the output would be the written text response from the LLM. Different LLMs were used, as I was unsure which models/APIs supported fine-tuning, but I settled on the Gemini-2.0-flash model, using the Vertex AI SDK. 


### Training


![Model fine tuning loss.](/Images/_train_total_loss.png)




### Performance Comparison


![Initial model accuracy (calculated using python scripts to parse responses, may include errors).](/Images/initial_accuracy.png)




![Fine-tuned model accuracy during training.](/Images/Accuracy.png)




### Conclusions

LLMs seem to be very capable with multimodal tasks (such as analyzing and describing an image), with initial tests having near perfect scores for "counting" shapes (averaging approximately 80% accuracy). This is very promising for higher order, more complex tasks, such as identifying or counting abnormalities, such as that in medical imaging. Although the fine-tuned LLM model wasn't tested properly, its increased training accuracy (approximately 93%) suggests favorable outcomes. 


### Future Work

In the future, I'd like to try a wider variety of conditions for fine-tuning (e.g., training on 10 vs. 20 images, different models), as well as conduct full post–fine-tuning evaluation on a left-out test set to verify improvements beyond training accuracy.




## How to Reproduce Results

To reproduce the analysis and modeling results:
* Clone this repository.
* Run `LLM_Image_Generation.ipynb` to generate shape image data
* Label data with Google Cloud's Vertex AI Studio
* Test and fine_tune data using guidance from `LLM_Initial.ipynb` and `LLM_Prototype.ipynb`

**Note: All steps/modeling require a Google Cloud account and proper personalization of existing code.* 


### Contents of Repository
* **LLM_Image_Generation.ipynb**: creation of datasets
* **LLM_Images.py**: modularized set of functions used to generate dataset images (based on code from `LLM_Image_Generation.ipynb`)
* **LLM_Test_API.ipynb**: initial tryout of an LLM API
* **LLM_Initial.ipynb**: initial attempt at collecting/recording data and LLM responses
* **LLM_Prototype.ipynb**: contains attempt to test, train, and fine-tune LLM models 


### Software Setup
Models were accessed through the Vertex AI SDK or Gemini API. Data was generated using matplotlib, and responses were stored with pandas.

### Data

Data can be generated using the code/guidance in `LLM_Image_Generation.ipynb` and `LLM_Images.py`.
