<div align="left" style="position: relative;">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="right" width="30%" style="margin: -20px 0 0 20px;">
<h1>DOG-CAT-IMAGE-CLASSIFICATION</h1>
<p align="left">
	<img src="https://img.shields.io/github/last-commit/Yoyobun1/Dog-cat-image-classification?style=social&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Yoyobun1/Dog-cat-image-classification?style=social&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Yoyobun1/Dog-cat-image-classification?style=social&color=0080ff" alt="repo-language-count">
</p>
<p align="left">Built with the tools and technologies:</p>
<p align="left">
	<img src="https://img.shields.io/badge/TensorFlow-FF6F00.svg?style=social&logo=TensorFlow&logoColor=white" alt="TensorFlow">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=social&logo=Python&logoColor=white" alt="Python">
</p>
</div>
<br clear="right">

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

This project implements a deep learning model using Convolutional Neural Networks (CNN) to classify images of cats and dogs. The dataset consists of labeled images, and the model is trained to predict the class (cat or dog) based on image features. The project involves steps like data preprocessing, model training, evaluation, and optimization for better accuracy.

---

## 👾 Features

- **Image Classification**: Classify images of cats and dogs using a Convolutional Neural Network (CNN).
- **Data Preprocessing**: Includes data cleaning, normalization, and augmentation techniques to enhance model performance.
- **Model Training**: Trains a CNN model using a dataset of labeled images.
- **Model Evaluation**: Evaluates the model's accuracy and performance on a test dataset.
- **Optimization**: Implements techniques to improve the model's accuracy and reduce overfitting.


---

## 📁 Project Structure

```sh
└── Dog-cat-image-classification/
    ├── Procfile
    ├── dogs_vs_cats.ipynb
    ├── prediction_cat.jpg
    ├── prediction_dog.jpeg
    ├── requirements.txt
    ├── setup.py
    ├── src
    │   └── __init__.py
    ├── test_set
    │   └── test_set
    └── training_set
        └── training_set
```


### 📂 Project Index
<details open>
	<summary><b><code>DOG-CAT-IMAGE-CLASSIFICATION/</code></b></summary>
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Yoyobun1/Dog-cat-image-classification/blob/master/Procfile'>Procfile</a></b></td>
				<td><code>❯ Used for deployment configuration (Heroku or similar services)</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Yoyobun1/Dog-cat-image-classification/blob/master/dogs_vs_cats.ipynb'>dogs_vs_cats.ipynb</a></b></td>
				<td><code>❯ Jupyter notebook for training and evaluating the CNN model</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Yoyobun1/Dog-cat-image-classification/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td><code>❯ Lists all Python dependencies for the project</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Yoyobun1/Dog-cat-image-classification/blob/master/setup.py'>setup.py</a></b></td>
				<td><code>❯ Python setup script for package installation</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details>
		<summary><b>test_set</b></summary>
		<blockquote>
			<details>
				<summary><b>test_set</b></summary>
				<blockquote>
					<details>
						<summary><b>cats</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Yoyobun1/Dog-cat-image-classification/blob/master/test_set/test_set/cats/_DS_Store'>_DS_Store</a></b></td>
								<td><code>❯ Metadata file for macOS directory</code></td>
							</tr>
							</table>
						</blockquote>
					</details>
					<details>
						<summary><b>dogs</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Yoyobun1/Dog-cat-image-classification/blob/master/test_set/test_set/dogs/_DS_Store'>_DS_Store</a></b></td>
								<td><code>❯ Metadata file for macOS directory</code></td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details>
		<summary><b>training_set</b></summary>
		<blockquote>
			<details>
				<summary><b>training_set</b></summary>
				<blockquote>
					<details>
						<summary><b>cats</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Yoyobun1/Dog-cat-image-classification/blob/master/training_set/training_set/cats/_DS_Store'>_DS_Store</a></b></td>
								<td><code>❯ Metadata file for macOS directory</code></td>
							</tr>
							</table>
						</blockquote>
					</details>
					<details>
						<summary><b>dogs</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Yoyobun1/Dog-cat-image-classification/blob/master/training_set/training_set/dogs/_DS_Store'>_DS_Store</a></b></td>
								<td><code>❯ Metadata file for macOS directory</code></td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>


---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with Dog-cat-image-classification, ensure your runtime environment meets the following requirements:

- **Programming Language:** JupyterNotebook
- **Package Manager:** Pip


### ⚙️ Installation

Install Dog-cat-image-classification using one of the following methods:

**Build from source:**

1. Clone the Dog-cat-image-classification repository:
```sh
❯ git clone https://github.com/Yoyobun1/Dog-cat-image-classification
```

2. Navigate to the project directory:
```sh
❯ cd Dog-cat-image-classification
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="" />]()

```sh
❯ echo 'INSERT-INSTALL-COMMAND-HERE'
```




### 🤖 Usage
Run Dog-cat-image-classification using the following command:
**Using `pip`** &nbsp; [<img align="center" src="" />]()

```sh
❯ echo 'INSERT-RUN-COMMAND-HERE'
```


### 🧪 Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="" />]()

```sh
❯ echo 'INSERT-TEST-COMMAND-HERE'
```


---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/Yoyobun1/Dog-cat-image-classification/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/Yoyobun1/Dog-cat-image-classification/issues)**: Submit bugs found or log feature requests for the `Dog-cat-image-classification` project.
- **💡 [Submit Pull Requests](https://github.com/Yoyobun1/Dog-cat-image-classification/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/Yoyobun1/Dog-cat-image-classification
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/Yoyobun1/Dog-cat-image-classification/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Yoyobun1/Dog-cat-image-classification">
   </a>
</p>
</details>

---



## 🙌 Acknowledgments
Get the full tutorial here: https://www.youtube.com/watch?v=0K4J_PTgysc

---
