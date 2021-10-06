# Setup:

* Create python environment:
```bash
virtualenv venv
```

* Activate environment: 
```bash
source venv/bin/activate
```

* Install requirements:
```bash
pip install -r requirements.txt
```

* Install chaostoolkit example plugin
```bash
pip install -e ./playground-plugin
```

* Run the experiment with settings.yaml:
```bash
chaos --settings=settings.yaml run exp.json
```