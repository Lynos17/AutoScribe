# AutoScribe
"Smarter Healthcare. One form at a time."


## Overview
AutoScribe is a smart, offline-first, gamified paperwork automation tool designed to:  
- Digitise handwritten and printed forms (e.g., patient intake, medication records).  
- Automate data entry into EHR systems, even in low-resource settings.  
- Gamify staff adoption with rewards for high-quality submissions.  

By automating repetitive tasks, AutoScribe helps hospitals and clinics save time, reduce errors, and improve patient care.  


## Features  
- OCR Pipeline: Digitise handwritten and printed forms using Tesseract OCR.  
- Offline Functionality: Store data locally and sync with EHR systems when online.  
- Data Mapping: Auto-fill EHR fields using regex.  
- Error Detection: Flag incomplete or inconsistent data for correction.  
- Gamified Adoption: Staff earn rewards for high-quality submissions.


## Installation
### Prerequisites
- Python 3.8 or higher
- Tesseract OCR installed in your system
  

### Steps
1. Clone this repository:  
   ```bash
   git clone https://github.com/Lynos17/AutoScribe.git  

2. Navigate to the project folder:
 cd AutoScribe

3. Install dependencies:
 pip install -r requirements.txt

4. Run the app:
python autoscribe.py

5. Usage of AutoScribe:
      1. Scan a Form: Use your phone or scanner to capture a form.  
      2. Upload the Image: Drag and drop the image into the AutoScribe app.  
      3. Review and Correct: Check the extracted data and correct any errors.  
      4. Submit Data: AutoScribe will auto-fill the EHR fields and sync the data when online.  
      5. View Dashboard: Open the Streamlit dashboard to see real-time insights.  


## Contributing  
We welcome contributions! Here’s how you can help:   
- Suggest Features: Share your ideas for new features or enhancements.  


## License  
AutoScribe is licensed under the MIT License. See [LICENSE](LICENSE) for more details.  


## Acknowledgments  
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for text recognition.  
- [Streamlit](https://streamlit.io/) for the dashboard.  
- [Kaggle IAM Handwriting Database](https://www.kaggle.com/datasets/nibinv23/iam-handwriting-word-database/) for training data.  


## Contact Information
For questions or collaborations, feel free to reach out:  
- Email: alfredndou51@gmail.com  
- GitHub: [Lynos17](https://github.com/Lynos17/)