# Setup:

* Clone and enter the repository:
```bash
git clone git@github.com:WixoLeo/ctk-tests.git && cd ctk-tests
```

* Checkout this branch:
```bash
git checkout activity-result
```

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
chaos run exp.json
```