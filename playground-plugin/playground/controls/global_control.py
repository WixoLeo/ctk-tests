from typing import Any
from typing import Dict
from typing import List

from chaoslib.types import Activity
from chaoslib.types import Configuration
from chaoslib.types import Experiment
from chaoslib.types import Hypothesis
from chaoslib.types import Journal
from chaoslib.types import Run
from chaoslib.types import Secrets
from chaoslib.types import Settings


# def configure_control(
#     configuration: Configuration,
#     secrets: Secrets,
#     settings: Settings,
#     experiment: Experiment,
# ):
#     print("GLOBAL configure control")


# def before_experiment_control(
#     context: Experiment,
#     configuration: Configuration,
#     secrets: Secrets,
#     settings: Settings,
#     experiment: Experiment,
#     **kwargs,
# ):
#     print("GLOBAL before experiment control")


# def after_experiment_control(
#     *,
#     context: Experiment,
#     state: Journal,
#     configuration: Configuration,
#     secrets: Secrets,
#     **kwargs,
# ):
#     print("GLOBAL after experiment control")


# def before_hypothesis_control(
#     *,
#     context: Hypothesis,
#     configuration: Configuration,
#     secrets: Secrets,
#     **kwargs,
# ):
#     print("GLOBAL before hypothesis control")


# def after_hypothesis_control(
#     *,
#     context: Hypothesis,
#     state: Dict[str, Any],
#     configuration: Configuration,
#     secrets: Secrets,
#     **kwargs,
# ):
#     print("GLOBAL after hypothesis control")


# def before_method_control(
#     *,
#     context: Experiment,
#     configuration: Configuration,
#     secrets: Secrets,
#     settings: Settings,
#     experiment: Experiment,
#     **kwargs,
# ):
#   print("GLOBAL before method control")


# def after_method_control(
#     *,
#     context: Experiment,
#     state: List[Run],
#     configuration: Configuration,
#     secrets: Secrets,
#     **kwargs,
# ):
#     print("GLOBAL after method control")


# def before_rollback_control(
#     *,
#     context: Experiment,
#     configuration: Configuration,
#     secrets: Secrets,
#     **kwargs,
# ):
#     print("GLOBAL before rollback control")


# def after_rollback_control(
#     *,
#     context: Experiment,
#     state: List[Run],
#     configuration: Configuration,
#     secrets: Secrets,
#     **kwargs,
# ):
#     print("GLOBAL after rollback control")


# def before_activity_control(
#     *,
#     context: Activity,
#     configuration: Configuration,
#     secrets: Secrets,
#     **kwargs,
# ):
#     print("GLOBAL before activity control")


# def after_activity_control(
#     *,
#     context: Activity,
#     state: Run,
#     configuration: Configuration,
#     secrets: Secrets,
#     **kwargs,
# ):
#     print("GLOBAL after activity control")


# def before_loading_experiment_control(
#     context: str,
# ):
#     print("GLOBAL before loading experiment control")


# def after_loading_experiment_control(
#     context: str,
#     state: Experiment,
# ):
#     # for _ in range(10):
#     #   state["controls"].append({
#     #     "name": "Playground control",
#     #     "provider": {
#     #       "type": "python",
#     #       "module": "playground.controls.playground_control"
#     #     }
#     #   })
#     print("GLOBAL after loading experiment control")