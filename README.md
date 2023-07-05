# Passengers classifire

## Project

- `Analysis`: data analysis and design model
- - `data_analysis_avia_clients.ipynb`: analysis raw data and preparation
- - `avia_classifier_fin.ipynb`: ml modelling
- `data`: different files for app
- `model.py`: model
- `functions.py`: functions for app
- `streamlit_app.py`: app


## Service:
Streamlit service is available at [passenger-satisfaction-pred.streamlit.app](https://passenger-satisfaction-pred.streamlit.app/) via Streamlit Cloud

To run locally, clone the repo and do the following:
```
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ streamlit run streamlit_app.py
```
The app will be available at `http://localhost:8501`
