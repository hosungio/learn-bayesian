from framework import SimpleBayesEstimator

if __name__ == "__main__":
    e = SimpleBayesEstimator(
        priors={"쇼핑족": 0.2, "아이쇼핑족": 0.8},
        conditional_probs={
            "쇼핑족": [("말을 걸 확률", 0.9), ("말을 걸지 않을 확률", 0.1)],
            "아이쇼핑족": [("말을 걸 확률", 0.3), ("말을 걸지 않을 확률", 0.7)],
        },
    )
    e.cal_all_probs()
