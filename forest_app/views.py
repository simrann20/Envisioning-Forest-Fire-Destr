from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
import pickle
from .forms import InputForm
import csv
# Create your views here.


def index(request):
    if request.method == "GET":
        form = InputForm()
        button_show = 'Yes'
        return render(request, 'index.html',{'form':form,'button_show':button_show})
    if request.method == 'POST':
        print(request.POST['x_coordinate'])
        row_heading = ['X','Y','month','day','FFMC','DMC','DC','ISI','temp','RH','wind','rain']
        row = [request.POST['x_coordinate'],request.POST['y_coordinate'],request.POST['month'],request.POST['day'],request.POST['ffmc'],request.POST['dmc'],request.POST['dc'],request.POST['isi'],request.POST['temp'],request.POST['rh'],request.POST['wind'],request.POST['outside'],]
        with open('input_file.csv', 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row_heading)
            writer.writerow(row)
            print("csvfile :",csvFile)
        csvFile.close()

    import pandas as pd
    import numpy as np
    from sklearn.metrics import mean_squared_error
    df_forest = pd.read_csv("forestfires.csv")
    df_forest['area'] = np.log(df_forest['area'] + 1)
    df_forest_input = pd.read_csv("input_file.csv")
    from sklearn.preprocessing import LabelEncoder
    categorical = list(df_forest.select_dtypes(include = ["object"]).columns)
    categorical_input = list(df_forest_input.select_dtypes(include = ["object"]).columns)

    for i, column in enumerate(categorical) :
        label = LabelEncoder()
        df_forest[column] = label.fit_transform(df_forest[column])
    for i, column in enumerate(categorical_input) :
        label = LabelEncoder()
        df_forest_input[column] = label.fit_transform(df_forest_input[column])


    outcome = df_forest['area']
    features = df_forest.iloc[:, :-1]

    features_input = df_forest_input.iloc[:, :]
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(features, outcome, test_size = 0.15, random_state = 196)

    from sklearn.svm import SVR
    model_4 = SVR(C = 100, kernel = 'linear')
    model_4.fit(X_train, y_train)

    prediction = model_4.predict(X_test)
    prediction_input = model_4.predict(features_input)
    mean_squared_error(y_test, prediction)
    prediction = np.exp(prediction - 1)
    prediction_input = np.exp(prediction_input - 1)
    print("prediction :",prediction)
    print("prediction_input :",str(prediction_input))
    output = str(prediction_input)
    button_show = 'No'
    return render(request, 'index.html',{'output':output,'button_show':button_show})











def predict(request):





    # df_forest = pd.read_csv("forestfires.csv")
    # df_forest['area'] = np.log(df_forest['area'] + 1)
    #
    # categorical = list(df_forest.select_dtypes(include = ["object"]).columns)
    #
    # for i, column in enumerate(categorical) :
    #     label = LabelEncoder()
    #     df_forest[column] = label.fit_transform(df_forest[column])
    #
    #
    # outcome = df_forest['area']
    # features = df_forest.iloc[:, :-1]
    #
    #
    # X_train, X_test, y_train, y_test = train_test_split(features, outcome, test_size = 0.15, random_state = 196)
    #
    #
    # model_4 = SVR(C = 100, kernel = 'linear')
    # model_4.fit(X_train, y_train)
    #
    # prediction = model_4.predict(X_test)
    # mean_squared_error(y_test, prediction)
    # prediction = np.exp(prediction - 1)


    # pickle_out = open("model.pkl", "wb")
    # pickle.dump(model_4, pickle_out)
    # pickle_out.close()


    return render(request, 'predict.html')
