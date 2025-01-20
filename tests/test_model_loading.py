import pickle


# to confirm model exists and can be loaded
def test_model_loading():
    with open('linear_model.pkl', 'rb') as f:
        model = pickle.load(f)
    assert model is not None
