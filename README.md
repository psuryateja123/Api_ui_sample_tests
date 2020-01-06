# Api_ui_sample_tests

#### Test Guidance

#### The tests in this framework are written in BDD (behave) pattern using feature file.

#### To clone the project 
```
https://github.com/psuryateja123/Api_ui_sample_tests.git
```

#### Installation: The required dependencies can be installed by 
* Type
```
pip install -r requirements.txt
```

* If there are any issues in installing the dependencies, they can be installed seperately using 
```
pip install name_of_the_dependency
```

#### Project Structure: 

* This project has the following folders

* [features](features) folder and it has all the feature files and another folder [Steps](features/steps).
* [pages](pages)
* [Steps](features/steps)
* [Utils](utils)
* [Locators](locators)

#### [Feature files](features)
* In this folder, there are two feature files.
* [API Test](features/api_tests.feature): This feature file has all the scenarios api automation.
* [UI Test](features/ui_test.feature): This feature file has all the scenarios, UI tests.

#### [Page objects](pages)
* It has a class, 
* In [ui_test_pageobject](pages/ui_test_pageObjects.py), I have placed the methods that are related to the News search.

#### [Step definitions](features/steps)
* It has two step definition files
* [API stepsDefs](features/steps/api_test_stepDefs.py) is related to [API Test](features/api_tests.feature).
* [UI stepDefs](features/steps/ui_test_stepDefs.py)is related to [UI Test](features/ui_test.feature)

#### [Utils](utils): 
* In this folder there are two class, they are the supporting class for the project.
* [actions](utils/actions.py) it has all the driver and other definitions that can be used through out the project.

#### Running tests: Considered that you have already cloned the project. You can run tests by typing behave in the commandline

* Type
```
behave
```
* To run specific tests using tags
```
behave --tags=@NAME_OF_THE_TAG
```

* In this project, I have configured two tags, @ui_test - for running all the tests related to the UI and the @api_test for runnging all the tests related to API.

* All the UI tests will run on a chrome browser.

Also integrated [Allure report](https://docs.qameta.io/allure/). This acts like a runner and also helps to generate reports.

* To run specific tests by using tags
```
behave --tags=@NAME_OF_THE_TAG -f allure_behave.formatter:AllureFormatter -o RESULTS_FOLDER ./features

```
* In this project, 

```
behave --tags=@ui_test -f allure_behave.formatter:AllureFormatter -o RESULTS_FOLDER ./features

```

* To view results, after running the tests

```
allure serve RESULTS_FOLDER
```
