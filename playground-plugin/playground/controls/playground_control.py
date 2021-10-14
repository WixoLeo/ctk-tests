from chaoslib.types import Activity
from chaoslib.types import Configuration
from chaoslib.types import Run
from chaoslib.types import Secrets

def after_activity_control(
    context: Activity,
    state: Run,
    configuration: Configuration,
    secrets: Secrets,
    **kwargs,
):
    print(f"Activity ended with result {state.get('status')}")
