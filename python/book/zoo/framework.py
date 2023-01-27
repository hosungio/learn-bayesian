"""
framework
"""

from typing import Dict
from typing import List
from typing import Tuple


class SimpleBayesEstimator:
    """Simple Bayes Estimator"""

    def __init__(
        self,
        priors: Dict[str, float],
        conditional_probs: Dict[str, List[Tuple[str, float]]],
    ) -> None:
        self._priors = priors
        self._conditional_probs = conditional_probs
        self._all_probs = {}

    def cal_all_probs(self) -> None:
        for prior_name, prior_prob in self._priors.items():
            for cond_name, cond_prob in self._conditional_probs[prior_name]:
                print(prior_name, cond_name, cond_prob)
                # key = f"{prior_name}_{}"
