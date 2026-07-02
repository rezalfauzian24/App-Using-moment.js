{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "name": "app.py",
      "include_colab_link": True
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rezalfauzian24/App-Using-moment.js/blob/main/app_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Loan_Prediction_Project**"
      ],
      "metadata": {
        "id": "9g3MeRIGP7L8"
      }
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_E98cf88hv-5",
        "outputId": "ac925f31-5f7f-4572-d1b2-2db180e3555d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Loan_ID', 'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area', 'Loan_Status']\n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "\n",
        "df = pd.read_csv('Loan_Prediction_Dataset.csv')\n",
        "\n",
        "print(df.columns.tolist())"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **STEP 1 — Load Dataset**"
      ],
      "metadata": {
        "id": "ayhGgPR1mAVe"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "df = pd.read_csv('Loan_Prediction_Dataset.csv')\n",
        "\n",
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 244
        },
        "id": "xDU04Iicl7T8",
        "outputId": "48001d27-e37b-4d15-87cf-d1dd942352c6"
      },
      "execution_count": None,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "    Loan_ID Gender Married Dependents     Education Self_Employed  \\\n",
              "0  LP001002   Male      No          0      Graduate            No   \n",
              "1  LP001003   Male     Yes          1      Graduate            No   \n",
              "2  LP001005   Male     Yes          0      Graduate           Yes   \n",
              "3  LP001006   Male     Yes          0  Not Graduate            No   \n",
              "4  LP001008   Male      No          0      Graduate            No   \n",
              "\n",
              "   ApplicantIncome  CoapplicantIncome  LoanAmount  Loan_Amount_Term  \\\n",
              "0             5849                0.0         NaN             360.0   \n",
              "1             4583             1508.0       128.0             360.0   \n",
              "2             3000                0.0        66.0             360.0   \n",
              "3             2583             2358.0       120.0             360.0   \n",
              "4             6000                0.0       141.0             360.0   \n",
              "\n",
              "   Credit_History Property_Area Loan_Status  \n",
              "0             1.0         Urban           Y  \n",
              "1             1.0         Rural           N  \n",
              "2             1.0         Urban           Y  \n",
              "3             1.0         Urban           Y  \n",
              "4             1.0         Urban           Y  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-d30396e3-bba8-4977-bfe0-91d7c8eca508\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Loan_ID</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Married</th>\n",
              "      <th>Dependents</th>\n",
              "      <th>Education</th>\n",
              "      <th>Self_Employed</th>\n",
              "      <th>ApplicantIncome</th>\n",
              "      <th>CoapplicantIncome</th>\n",
              "      <th>LoanAmount</th>\n",
              "      <th>Loan_Amount_Term</th>\n",
              "      <th>Credit_History</th>\n",
              "      <th>Property_Area</th>\n",
              "      <th>Loan_Status</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>LP001002</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>5849</td>\n",
              "      <td>0.0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>LP001003</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>1</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>4583</td>\n",
              "      <td>1508.0</td>\n",
              "      <td>128.0</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Rural</td>\n",
              "      <td>N</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>LP001005</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>Yes</td>\n",
              "      <td>3000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>66.0</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>LP001006</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Not Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>2583</td>\n",
              "      <td>2358.0</td>\n",
              "      <td>120.0</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>LP001008</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>6000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>141.0</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-d30396e3-bba8-4977-bfe0-91d7c8eca508')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-d30396e3-bba8-4977-bfe0-91d7c8eca508 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-d30396e3-bba8-4977-bfe0-91d7c8eca508');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 614,\n  \"fields\": [\n    {\n      \"column\": \"Loan_ID\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 614,\n        \"samples\": [\n          \"LP002139\",\n          \"LP002223\",\n          \"LP001570\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Gender\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Female\",\n          \"Male\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Married\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Yes\",\n          \"No\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Dependents\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 4,\n        \"samples\": [\n          \"1\",\n          \"3+\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Education\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Not Graduate\",\n          \"Graduate\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Self_Employed\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Yes\",\n          \"No\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"ApplicantIncome\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 6109,\n        \"min\": 150,\n        \"max\": 81000,\n        \"num_unique_values\": 505,\n        \"samples\": [\n          8333,\n          4342\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"CoapplicantIncome\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 2926.2483692241917,\n        \"min\": 0.0,\n        \"max\": 41667.0,\n        \"num_unique_values\": 287,\n        \"samples\": [\n          1840.0,\n          2042.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"LoanAmount\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 85.58732523570545,\n        \"min\": 9.0,\n        \"max\": 700.0,\n        \"num_unique_values\": 203,\n        \"samples\": [\n          100.0,\n          70.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Loan_Amount_Term\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 65.12040985461256,\n        \"min\": 12.0,\n        \"max\": 480.0,\n        \"num_unique_values\": 10,\n        \"samples\": [\n          84.0,\n          120.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Credit_History\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.3648783192364049,\n        \"min\": 0.0,\n        \"max\": 1.0,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          0.0,\n          1.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Property_Area\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 3,\n        \"samples\": [\n          \"Urban\",\n          \"Rural\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Loan_Status\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"N\",\n          \"Y\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **STEP 2 — Basic Information**"
      ],
      "metadata": {
        "id": "UnrLg3wMnfnN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SXR3kPOoneLT",
        "outputId": "98dff822-ee43-4b1d-a671-8fadbd50ec77"
      },
      "execution_count": None,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 614 entries, 0 to 613\n",
            "Data columns (total 13 columns):\n",
            " #   Column             Non-Null Count  Dtype  \n",
            "---  ------             --------------  -----  \n",
            " 0   Loan_ID            614 non-null    object \n",
            " 1   Gender             601 non-null    object \n",
            " 2   Married            611 non-null    object \n",
            " 3   Dependents         599 non-null    object \n",
            " 4   Education          614 non-null    object \n",
            " 5   Self_Employed      582 non-null    object \n",
            " 6   ApplicantIncome    614 non-null    int64  \n",
            " 7   CoapplicantIncome  614 non-null    float64\n",
            " 8   LoanAmount         592 non-null    float64\n",
            " 9   Loan_Amount_Term   600 non-null    float64\n",
            " 10  Credit_History     564 non-null    float64\n",
            " 11  Property_Area      614 non-null    object \n",
            " 12  Loan_Status        614 non-null    object \n",
            "dtypes: float64(4), int64(1), object(8)\n",
            "memory usage: 62.5+ KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ls24QcEAoBXY",
        "outputId": "4170880d-cd27-4514-ca8e-128749ae9a0b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(614, 13)"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **STEP 3 — Check Missing Values**"
      ],
      "metadata": {
        "id": "EkHBHsExoblA"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df.isnull().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 492
        },
        "id": "frq71jKVoaID",
        "outputId": "fb6aeae1-3466-462b-9073-838f9e2397e0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Loan_ID               0\n",
              "Gender               13\n",
              "Married               3\n",
              "Dependents           15\n",
              "Education             0\n",
              "Self_Employed        32\n",
              "ApplicantIncome       0\n",
              "CoapplicantIncome     0\n",
              "LoanAmount           22\n",
              "Loan_Amount_Term     14\n",
              "Credit_History       50\n",
              "Property_Area         0\n",
              "Loan_Status           0\n",
              "dtype: int64"
            ],
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>0</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Loan_ID</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Gender</th>\n",
              "      <td>13</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Married</th>\n",
              "      <td>3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Dependents</th>\n",
              "      <td>15</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Education</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Self_Employed</th>\n",
              "      <td>32</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>ApplicantIncome</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>CoapplicantIncome</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>LoanAmount</th>\n",
              "      <td>22</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Loan_Amount_Term</th>\n",
              "      <td>14</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Credit_History</th>\n",
              "      <td>50</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Property_Area</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Loan_Status</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> int64</label>"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **STEP 4 — Data Cleaning**"
      ],
      "metadata": {
        "id": "w6kW4Kigo0Uc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)\n",
        "\n",
        "df['Married'].fillna(df['Married'].mode()[0], inplace=True)\n",
        "\n",
        "df['Dependents'].fillna(df['Dependents'].mode()[0], inplace=True)\n",
        "\n",
        "df['Self_Employed'].fillna(df['Self_Employed'].mode()[0], inplace=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_JDns7c5ozVD",
        "outputId": "72a7a51a-1c60-48fe-fa1b-407a1eb63b87"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/tmp/ipykernel_3920/1651490757.py:1: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.\n",
            "The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.\n",
            "\n",
            "For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.\n",
            "\n",
            "\n",
            "  df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)\n",
            "/tmp/ipykernel_3920/1651490757.py:3: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.\n",
            "The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.\n",
            "\n",
            "For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.\n",
            "\n",
            "\n",
            "  df['Married'].fillna(df['Married'].mode()[0], inplace=True)\n",
            "/tmp/ipykernel_3920/1651490757.py:5: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.\n",
            "The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.\n",
            "\n",
            "For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.\n",
            "\n",
            "\n",
            "  df['Dependents'].fillna(df['Dependents'].mode()[0], inplace=True)\n",
            "/tmp/ipykernel_3920/1651490757.py:7: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.\n",
            "The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.\n",
            "\n",
            "For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.\n",
            "\n",
            "\n",
            "  df['Self_Employed'].fillna(df['Self_Employed'].mode()[0], inplace=True)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**We Fill numerical columns:**"
      ],
      "metadata": {
        "id": "_0-JOAzjpCJo"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df['LoanAmount'].fillna(df['LoanAmount'].median(), inplace=True)\n",
        "\n",
        "df['Loan_Amount_Term'].fillna(\n",
        "    df['Loan_Amount_Term'].median(),\n",
        "    inplace=True\n",
        ")\n",
        "\n",
        "df['Credit_History'].fillna(\n",
        "    df['Credit_History'].mode()[0],\n",
        "    inplace=True\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "niZxe7EppFRp",
        "outputId": "5db67da2-bbcf-47a2-cb19-9fab4bb58d0f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/tmp/ipykernel_3920/2385275985.py:1: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.\n",
            "The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.\n",
            "\n",
            "For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.\n",
            "\n",
            "\n",
            "  df['LoanAmount'].fillna(df['LoanAmount'].median(), inplace=True)\n",
            "/tmp/ipykernel_3920/2385275985.py:3: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.\n",
            "The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.\n",
            "\n",
            "For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.\n",
            "\n",
            "\n",
            "  df['Loan_Amount_Term'].fillna(\n",
            "/tmp/ipykernel_3920/2385275985.py:8: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.\n",
            "The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.\n",
            "\n",
            "For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.\n",
            "\n",
            "\n",
            "  df['Credit_History'].fillna(\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Verify:**\n",
        "\n",
        "after Data Cleaning and Filling numerical columns."
      ],
      "metadata": {
        "id": "RdlCvxVCpHoF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df.isnull().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 492
        },
        "id": "cmTOJTZApQ2r",
        "outputId": "2ba23fbe-ea76-4406-883d-65efd5e80ff4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Loan_ID              0\n",
              "Gender               0\n",
              "Married              0\n",
              "Dependents           0\n",
              "Education            0\n",
              "Self_Employed        0\n",
              "ApplicantIncome      0\n",
              "CoapplicantIncome    0\n",
              "LoanAmount           0\n",
              "Loan_Amount_Term     0\n",
              "Credit_History       0\n",
              "Property_Area        0\n",
              "Loan_Status          0\n",
              "dtype: int64"
            ],
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>0</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Loan_ID</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Gender</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Married</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Dependents</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Education</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Self_Employed</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>ApplicantIncome</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>CoapplicantIncome</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>LoanAmount</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Loan_Amount_Term</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Credit_History</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Property_Area</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Loan_Status</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> int64</label>"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **STEP 5 — Brief Data Analysis**\n",
        "\n",
        "**Loan Approval Distribution **"
      ],
      "metadata": {
        "id": "_c9LfTIjqP2m"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "\n",
        "df['Loan_Status'].value_counts().plot(\n",
        "    kind='bar'\n",
        ")\n",
        "\n",
        "plt.title(\n",
        "    'Loan Approval Distribution'\n",
        ")\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 468
        },
        "id": "JkiyiyeJqPI5",
        "outputId": "828c97cb-cf1c-44cc-9a32-6dc61aae5eb1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAigAAAHDCAYAAAAOZuFZAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAN8lJREFUeJzt3XtcVXW+//E3qGxB3CAobBjwlpbitaOm+2jmLRHR0RHLHCexcbQMG5Mxzcm8NaVZZ7SL9zOpnXR09KGVNqloiWcSzSzzGpNmaiFQmmy1BIH1+6Mf67QFLyjKF309H4/1aK/v+q61PmsD7ndrfdfaPpZlWQIAADCIb3kXAAAAcDECCgAAMA4BBQAAGIeAAgAAjENAAQAAxiGgAAAA4xBQAACAcQgoAADAOAQUAABgHAIKgAph8eLF8vHx0ddff13m2x4yZIjq1q1b5tstSd26dTVkyBB7vui4Pvnkk5uy/06dOqlTp043ZV/A9SCg4JZ3sz8AytqcOXPk4+Ojtm3blncpFcLkyZPl4+NjTwEBAapdu7Z69+6tRYsWKTc3t0z2c+DAAU2ePPmGBKbrZXJtwNWqXN4FALi8pUuXqm7duvr444916NAhNWjQoLxLqhDmzp2rwMBA5ebm6ttvv9WGDRv0+9//XrNmzdK6desUHR1t9124cKEKCwtLtf0DBw5oypQp6tSpU6nOvqSnp8vX98b+v+Hlatu4ceMN3TdQVjiDAhjsyJEj2rZtm/7617+qVq1aWrp0abnVkp+fr7y8vHLbf2n1799fv/vd7zR06FBNnDhRH330kd566y3t27dPDzzwgFffKlWqyOFw3LBaLMvSTz/9JElyOByqUqXKDdvXlfj5+cnPz6/c9g9cLQIK8P999tlniouLk9PpVGBgoLp27art27d79Tl16pTGjBmjZs2aKTAwUE6nU3Fxcfr888+9+m3ZskU+Pj76xz/+oeeff15RUVGqWrWqunbtqkOHDl11TUuXLlWNGjUUHx+v/v37lxhQvv76a/n4+Ojll1/WzJkzVadOHfn7++u+++7Tvn37vPoOGTJEgYGB+uqrrxQbG6tq1aopMjJSU6dO1S+/2PyX25w1a5buuOMOORwOHThwQJL0wQcf6N5771W1atUUHBysPn366ODBg/b6q1atko+Pj1JTU4vVO3/+fPn4+Ni17dmzR0OGDFH9+vVVtWpVuVwu/f73v9fJkyev+n26WoMGDdIf/vAH7dixQykpKV7vy8VnGpYvX65WrVqpevXqcjqdatasmV555RVJP182LAo5nTt3ti8nbdmyRdLP40x69eqlDRs2qHXr1vL399f8+fPtZb8cg1Lkxx9/1KOPPqrQ0FA5nU4NHjxYP/zwg1cfHx8fTZ48udi6v9zmlWoraQxKdna2hg4dqvDwcFWtWlUtWrTQkiVLvPr88ndiwYIF9u9EmzZttHPnzhLfb+B6cIkHkLR//37de++9cjqdGjt2rKpUqaL58+erU6dOSk1Ntcd/fPXVV3r77bf1wAMPqF69esrKytL8+fN133336cCBA4qMjPTa7vTp0+Xr66sxY8YoJydHM2bM0KBBg7Rjx46rqmvp0qXq16+f/Pz8NHDgQM2dO1c7d+5UmzZtivV98803debMGSUlJen8+fN65ZVX1KVLF+3du1fh4eF2v4KCAvXo0UPt2rXTjBkztH79ek2aNEn5+fmaOnWq1zYXLVqk8+fPa/jw4XI4HAoJCdGmTZsUFxen+vXra/Lkyfrpp5/02muvqX379vr0009Vt25dxcfHKzAwUP/4xz903333eW1zxYoVatKkiZo2bSpJSklJ0VdffaVHHnlELpdL+/fv14IFC7R//35t375dPj4+V/VeXa2HH35YCxYs0MaNG3X//feX2CclJUUDBw5U165d9eKLL0qSDh48qI8++kijRo1Sx44d9cc//lGvvvqq/vznP6tx48aSZP9X+vlSzsCBA/Xoo49q2LBhuuuuuy5b18iRIxUcHKzJkycrPT1dc+fO1dGjR+2we7WuprZf+umnn9SpUycdOnRII0eOVL169bRy5UoNGTJEp0+f1qhRo7z6L1u2TGfOnNGjjz4qHx8fzZgxQ/369dNXX31VrmeGcAuygFvcokWLLEnWzp07L9mnb9++lp+fn3X48GG7LSMjw6pevbrVsWNHu+38+fNWQUGB17pHjhyxHA6HNXXqVLvtww8/tCRZjRs3tnJzc+32V155xZJk7d2794p1f/LJJ5YkKyUlxbIsyyosLLSioqKsUaNGFdu/JMvf39/65ptv7PYdO3ZYkqzRo0fbbYmJiZYk64knnrDbCgsLrfj4eMvPz8/67rvvvLbpdDqt7Oxsr/21bNnSCgsLs06ePGm3ff7555avr681ePBgu23gwIFWWFiYlZ+fb7edOHHC8vX19Xqvfvzxx2LH/ve//92SZG3dutVuK/o5Hjly5LLv26RJkyxJ9rFc7IcffrAkWb/5zW+83pc6derY86NGjbKcTqdX7RdbuXKlJcn68MMPiy2rU6eOJclav359icsSExOLHVerVq2svLw8u33GjBmWJOudd96x2yRZkyZNuuI2L1fbfffdZ9133332/KxZsyxJ1ltvvWW35eXlWW632woMDLQ8Ho9lWf/3OxEaGmqdOnXK7vvOO+9Ykqy1a9cW2xdwPbjEg9teQUGBNm7cqL59+6p+/fp2e0REhH7729/qX//6lzwej6Sfxw8UDXAsKCjQyZMnFRgYqLvuukuffvppsW0/8sgjXtf77733Xkk/n4m5kqVLlyo8PFydO3eW9PPp/QEDBmj58uUqKCgo1r9v37761a9+Zc/fc889atu2rf75z38W6zty5Ej7tY+Pj0aOHKm8vDxt2rTJq19CQoJq1aplz584cUK7d+/WkCFDFBISYrc3b95c999/v9e+BgwYoOzsbPvSgvTzpZ/CwkINGDDAbvP397dfnz9/Xt9//73atWsnSSW+p9crMDBQknTmzJlL9gkODta5c+e8LgOVVr169RQbG3vV/YcPH+51BmLEiBGqXLlyiT+/svTPf/5TLpdLAwcOtNuqVKmiP/7xjzp79myxy3QDBgxQjRo17PnS/E4DpUFAwW3vu+++048//ljiKfjGjRursLBQx48flyQVFhZq5syZatiwoRwOh2rWrKlatWppz549ysnJKbZ+7dq1veaL/mG/eGzBxQoKCrR8+XJ17txZR44c0aFDh3To0CG1bdtWWVlZ2rx5c7F1GjZsWKztzjvvLHarqa+vr1cQK+onqVjfevXqec0fPXpUki75Xn3//fc6d+6cJKlHjx4KCgrSihUr7D4rVqxQy5Yt7f1JP4/rGTVqlMLDw+Xv769atWrZ+y3pPb1eZ8+elSRVr179kn0ef/xx3XnnnYqLi1NUVJR+//vfa/369aXaz8Xv3ZVc/PMLDAxURETEDb9V+OjRo2rYsGGxO4uKLgkV/cyLXOvvNFBaBBSgFF544QUlJyerY8eOeuutt7RhwwalpKSoSZMmJd6mWqlSpRK3Y/1iQGpJPvjgA504cULLly9Xw4YN7enBBx+UpJt2N88vz26UlsPhUN++fbVmzRrl5+fr22+/1UcffeR19kSSHnzwQS1cuFCPPfaYVq9erY0bN9phoLS3/l6NosG5l7tdOywsTLt379a7776rX//61/rwww8VFxenxMTEq97P9bx3pVXSGbUb5Vp/p4HSYpAsbnu1atVSQECA0tPTiy374osv5Ovraz8zY9WqVercubP+9re/efU7ffq0atasWWY1LV26VGFhYZo9e3axZatXr9aaNWs0b948rw/BL7/8sljff//738XuTiksLNRXX33ldRbj3//+tyRd8XkederUkaRLvlc1a9ZUtWrV7LYBAwZoyZIl2rx5sw4ePCjLsrwCyg8//KDNmzdrypQpmjhx4mWPpaz8z//8jyRd8fKLn5+fevfurd69e6uwsFCPP/645s+fr2effVYNGjQo88G7X375pX05T/r5TM+JEyfUs2dPu61GjRo6ffq013p5eXk6ceKEV1tpaqtTp4727NmjwsJCr7MoX3zxhb0cKA+cQcFtr1KlSurevbveeecdr9PpWVlZWrZsmTp06CCn02n3vfj/FFeuXKlvv/22zOr56aeftHr1avXq1Uv9+/cvNo0cOVJnzpzRu+++67Xe22+/7VXHxx9/rB07diguLq7YPl5//XX7tWVZev3111WlShV17dr1srVFRESoZcuWWrJkidcH5b59+7Rx40avD1NJ6tatm0JCQrRixQqtWLFC99xzj9elj6L/G7/4PZ01a9Zl67hWy5Yt03//93/L7XZf9lgvvsXZ19dXzZs3lyT7SbRFQeziwHCtFixYoAsXLtjzc+fOVX5+vtfP74477tDWrVuLrXfxGZTS1NazZ09lZmZ6XYrLz8/Xa6+9psDAwGJ3YQE3C2dQcNt44403ShxHMGrUKP3lL39RSkqKOnTooMcff1yVK1fW/PnzlZubqxkzZth9e/XqpalTp+qRRx7Rf/7nf2rv3r1aunRpsTEd1+Pdd9/VmTNn9Otf/7rE5e3atbMf2vbLsxENGjRQhw4dNGLECOXm5mrWrFkKDQ3V2LFjvdavWrWq1q9fr8TERLVt21bvv/++3nvvPf35z3/2GhB7KS+99JLi4uLkdrs1dOhQ+zbjoKCgYs/oqFKlivr166fly5fr3Llzevnll72WO51OdezYUTNmzNCFCxf0q1/9Shs3btSRI0eu8t26tFWrVikwMFB5eXn2k2Q/+ugjtWjRQitXrrzsun/4wx906tQpdenSRVFRUTp69Khee+01tWzZ0h6b0bJlS1WqVEkvvviicnJy5HA41KVLF4WFhV1TvXl5eeratasefPBBpaena86cOerQoYPX78Ef/vAHPfbYY0pISND999+vzz//XBs2bCh29q40tQ0fPlzz58/XkCFDtGvXLtWtW1erVq3SRx99pFmzZl12rA5wQ5XnLUTAzVB0G+elpuPHj1uWZVmffvqpFRsbawUGBloBAQFW586drW3btnlt6/z589af/vQnKyIiwvL397fat29vpaWlFbt1s+g245UrV3qtX3Sr5qJFiy5Zb+/eva2qVata586du2SfIUOGWFWqVLG+//57e5svvfSS9V//9V9WdHS05XA4rHvvvdf6/PPPvdZLTEy0qlWrZh0+fNjq3r27FRAQYIWHh1uTJk3yun36l9ssyaZNm6z27dtb/v7+ltPptHr37m0dOHCgxL4pKSmWJMvHx8d+r3/pm2++sX7zm99YwcHBVlBQkPXAAw9YGRkZxW6pLe1txkVT1apVraioKKtXr17WG2+8YZ0/f77YOhffZrxq1Sqre/fuVlhYmOXn52fVrl3bevTRR60TJ054rbdw4UKrfv36VqVKlbxu661Tp44VHx9fYn2Xus04NTXVGj58uFWjRg0rMDDQGjRokNet3JZlWQUFBda4ceOsmjVrWgEBAVZsbKx16NChYtu8XG0X/65almVlZWVZjzzyiFWzZk3Lz8/PatasWbHf0cv9Tlz8swLKgo9lMbIJqMi+/vpr1atXTy+99JLGjBlz2b5DhgzRqlWr7DtZAMBUjEEBAADGIaAAAADjEFAAAIBxGIMCAACMwxkUAABgHAIKAAAwToV8UFthYaEyMjJUvXr1Mn/cNAAAuDEsy9KZM2cUGRlZ7AsqL1YhA0pGRob93SgAAKBiOX78uKKioi7bp0IGlKJHLx8/ftz+jhQAAGA2j8ej6Ojoq/oKhQoZUIou6zidTgIKAAAVzNUMz2CQLAAAMA4BBQAAGIeAAgAAjENAAQAAxiGgAAAA4xBQAACAcQgoAADAOAQUAABgHAIKAAAwDgEFAAAYh4ACAACMQ0ABAADGIaAAAADjEFAAAIBxKpd3ASiduk+/V94l4Cb6enp8eZcAAOWCMygAAMA4BBQAAGAcAgoAADAOAQUAABiHgAIAAIxDQAEAAMYhoAAAAOMQUAAAgHEIKAAAwDgEFAAAYBwCCgAAMA4BBQAAGIeAAgAAjENAAQAAxrmugDJ9+nT5+PjoySeftNvOnz+vpKQkhYaGKjAwUAkJCcrKyvJa79ixY4qPj1dAQIDCwsL01FNPKT8//3pKAQAAt5BrDig7d+7U/Pnz1bx5c6/20aNHa+3atVq5cqVSU1OVkZGhfv362csLCgoUHx+vvLw8bdu2TUuWLNHixYs1ceLEaz8KAABwS7mmgHL27FkNGjRICxcuVI0aNez2nJwc/e1vf9Nf//pXdenSRa1atdKiRYu0bds2bd++XZK0ceNGHThwQG+99ZZatmypuLg4Pffcc5o9e7by8vLK5qgAAECFdk0BJSkpSfHx8erWrZtX+65du3ThwgWv9kaNGql27dpKS0uTJKWlpalZs2YKDw+3+8TGxsrj8Wj//v0l7i83N1cej8drAgAAt67KpV1h+fLl+vTTT7Vz585iyzIzM+Xn56fg4GCv9vDwcGVmZtp9fhlOipYXLSvJtGnTNGXKlNKWCgAAKqhSnUE5fvy4Ro0apaVLl6pq1ao3qqZixo8fr5ycHHs6fvz4Tds3AAC4+UoVUHbt2qXs7Gz9x3/8hypXrqzKlSsrNTVVr776qipXrqzw8HDl5eXp9OnTXutlZWXJ5XJJklwuV7G7eormi/pczOFwyOl0ek0AAODWVaqA0rVrV+3du1e7d++2p9atW2vQoEH26ypVqmjz5s32Ounp6Tp27Jjcbrckye12a+/evcrOzrb7pKSkyOl0KiYmpowOCwAAVGSlGoNSvXp1NW3a1KutWrVqCg0NtduHDh2q5ORkhYSEyOl06oknnpDb7Va7du0kSd27d1dMTIwefvhhzZgxQ5mZmZowYYKSkpLkcDjK6LAAAEBFVupBslcyc+ZM+fr6KiEhQbm5uYqNjdWcOXPs5ZUqVdK6des0YsQIud1uVatWTYmJiZo6dWpZlwIAACooH8uyrPIuorQ8Ho+CgoKUk5Nz241Hqfv0e+VdAm6ir6fHl3cJAFBmSvP5zXfxAAAA4xBQAACAcQgoAADAOAQUAABgHAIKAAAwDgEFAAAYh4ACAACMQ0ABAADGIaAAAADjEFAAAIBxCCgAAMA4BBQAAGAcAgoAADAOAQUAABiHgAIAAIxDQAEAAMYhoAAAAOMQUAAAgHEIKAAAwDgEFAAAYBwCCgAAMA4BBQAAGIeAAgAAjENAAQAAxiGgAAAA4xBQAACAcQgoAADAOAQUAABgHAIKAAAwDgEFAAAYp1QBZe7cuWrevLmcTqecTqfcbrfef/99e3mnTp3k4+PjNT322GNe2zh27Jji4+MVEBCgsLAwPfXUU8rPzy+bowEAALeEyqXpHBUVpenTp6thw4ayLEtLlixRnz599Nlnn6lJkyaSpGHDhmnq1Kn2OgEBAfbrgoICxcfHy+Vyadu2bTpx4oQGDx6sKlWq6IUXXiijQwIAABVdqQJK7969veaff/55zZ07V9u3b7cDSkBAgFwuV4nrb9y4UQcOHNCmTZsUHh6uli1b6rnnntO4ceM0efJk+fn5XeNhAACAW8k1j0EpKCjQ8uXLde7cObndbrt96dKlqlmzppo2barx48frxx9/tJelpaWpWbNmCg8Pt9tiY2Pl8Xi0f//+S+4rNzdXHo/HawIAALeuUp1BkaS9e/fK7Xbr/PnzCgwM1Jo1axQTEyNJ+u1vf6s6deooMjJSe/bs0bhx45Senq7Vq1dLkjIzM73CiSR7PjMz85L7nDZtmqZMmVLaUgEAQAVV6oBy1113affu3crJydGqVauUmJio1NRUxcTEaPjw4Xa/Zs2aKSIiQl27dtXhw4d1xx13XHOR48ePV3Jysj3v8XgUHR19zdsDAABmK/UlHj8/PzVo0ECtWrXStGnT1KJFC73yyisl9m3btq0k6dChQ5Ikl8ulrKwsrz5F85catyJJDofDvnOoaAIAALeu634OSmFhoXJzc0tctnv3bklSRESEJMntdmvv3r3Kzs62+6SkpMjpdNqXiQAAAEp1iWf8+PGKi4tT7dq1debMGS1btkxbtmzRhg0bdPjwYS1btkw9e/ZUaGio9uzZo9GjR6tjx45q3ry5JKl79+6KiYnRww8/rBkzZigzM1MTJkxQUlKSHA7HDTlAAABQ8ZQqoGRnZ2vw4ME6ceKEgoKC1Lx5c23YsEH333+/jh8/rk2bNmnWrFk6d+6coqOjlZCQoAkTJtjrV6pUSevWrdOIESPkdrtVrVo1JSYmej03BQAAwMeyLKu8iygtj8ejoKAg5eTk3HbjUeo+/V55l4Cb6Ovp8eVdAgCUmdJ8fvNdPAAAwDgEFAAAYBwCCgAAMA4BBQAAGIeAAgAAjENAAQAAxiGgAAAA4xBQAACAcQgoAADAOAQUAABgHAIKAAAwDgEFAAAYh4ACAACMQ0ABAADGIaAAAADjEFAAAIBxCCgAAMA4BBQAAGAcAgoAADAOAQUAABiHgAIAAIxDQAEAAMYhoAAAAOMQUAAAgHEIKAAAwDgEFAAAYBwCCgAAMA4BBQAAGIeAAgAAjENAAQAAxiGgAAAA45QqoMydO1fNmzeX0+mU0+mU2+3W+++/by8/f/68kpKSFBoaqsDAQCUkJCgrK8trG8eOHVN8fLwCAgIUFhamp556Svn5+WVzNAAA4JZQqoASFRWl6dOna9euXfrkk0/UpUsX9enTR/v375ckjR49WmvXrtXKlSuVmpqqjIwM9evXz16/oKBA8fHxysvL07Zt27RkyRItXrxYEydOLNujAgAAFZqPZVnW9WwgJCREL730kvr3769atWpp2bJl6t+/vyTpiy++UOPGjZWWlqZ27drp/fffV69evZSRkaHw8HBJ0rx58zRu3Dh999138vPzu6p9ejweBQUFKScnR06n83rKr3DqPv1eeZeAm+jr6fHlXQIAlJnSfH5f8xiUgoICLV++XOfOnZPb7dauXbt04cIFdevWze7TqFEj1a5dW2lpaZKktLQ0NWvWzA4nkhQbGyuPx2OfhSlJbm6uPB6P1wQAAG5dpQ4oe/fuVWBgoBwOhx577DGtWbNGMTExyszMlJ+fn4KDg736h4eHKzMzU5KUmZnpFU6Klhctu5Rp06YpKCjInqKjo0tbNgAAqEBKHVDuuusu7d69Wzt27NCIESOUmJioAwcO3IjabOPHj1dOTo49HT9+/IbuDwAAlK/KpV3Bz89PDRo0kCS1atVKO3fu1CuvvKIBAwYoLy9Pp0+f9jqLkpWVJZfLJUlyuVz6+OOPvbZXdJdPUZ+SOBwOORyO0pYKAAAqqOt+DkphYaFyc3PVqlUrValSRZs3b7aXpaen69ixY3K73ZIkt9utvXv3Kjs72+6TkpIip9OpmJiY6y0FAADcIkp1BmX8+PGKi4tT7dq1debMGS1btkxbtmzRhg0bFBQUpKFDhyo5OVkhISFyOp164okn5Ha71a5dO0lS9+7dFRMTo4cfflgzZsxQZmamJkyYoKSkJM6QAAAAW6kCSnZ2tgYPHqwTJ04oKChIzZs314YNG3T//fdLkmbOnClfX18lJCQoNzdXsbGxmjNnjr1+pUqVtG7dOo0YMUJut1vVqlVTYmKipk6dWrZHBQAAKrTrfg5KeeA5KLhd8BwUALeSm/IcFAAAgBuFgAIAAIxDQAEAAMYhoAAAAOMQUAAAgHEIKAAAwDgEFAAAYBwCCgAAMA4BBQAAGIeAAgAAjENAAQAAxiGgAAAA4xBQAACAcQgoAADAOAQUAABgHAIKAAAwDgEFAAAYh4ACAACMQ0ABAADGIaAAAADjEFAAAIBxCCgAAMA4BBQAAGAcAgoAADAOAQUAABiHgAIAAIxDQAEAAMYhoAAAAOMQUAAAgHEIKAAAwDgEFAAAYJxSBZRp06apTZs2ql69usLCwtS3b1+lp6d79enUqZN8fHy8pscee8yrz7FjxxQfH6+AgACFhYXpqaeeUn5+/vUfDQAAuCVULk3n1NRUJSUlqU2bNsrPz9ef//xnde/eXQcOHFC1atXsfsOGDdPUqVPt+YCAAPt1QUGB4uPj5XK5tG3bNp04cUKDBw9WlSpV9MILL5TBIQEAgIquVAFl/fr1XvOLFy9WWFiYdu3apY4dO9rtAQEBcrlcJW5j48aNOnDggDZt2qTw8HC1bNlSzz33nMaNG6fJkyfLz8/vGg4DAADcSq5rDEpOTo4kKSQkxKt96dKlqlmzppo2barx48frxx9/tJelpaWpWbNmCg8Pt9tiY2Pl8Xi0f//+EveTm5srj8fjNQEAgFtXqc6g/FJhYaGefPJJtW/fXk2bNrXbf/vb36pOnTqKjIzUnj17NG7cOKWnp2v16tWSpMzMTK9wIsmez8zMLHFf06ZN05QpU661VAAAUMFcc0BJSkrSvn379K9//curffjw4fbrZs2aKSIiQl27dtXhw4d1xx13XNO+xo8fr+TkZHve4/EoOjr62goHAADGu6ZLPCNHjtS6dev04YcfKioq6rJ927ZtK0k6dOiQJMnlcikrK8urT9H8pcatOBwOOZ1OrwkAANy6ShVQLMvSyJEjtWbNGn3wwQeqV6/eFdfZvXu3JCkiIkKS5Ha7tXfvXmVnZ9t9UlJS5HQ6FRMTU5pyAADALapUl3iSkpK0bNkyvfPOO6pevbo9ZiQoKEj+/v46fPiwli1bpp49eyo0NFR79uzR6NGj1bFjRzVv3lyS1L17d8XExOjhhx/WjBkzlJmZqQkTJigpKUkOh6PsjxAAAFQ4pTqDMnfuXOXk5KhTp06KiIiwpxUrVkiS/Pz8tGnTJnXv3l2NGjXSn/70JyUkJGjt2rX2NipVqqR169apUqVKcrvd+t3vfqfBgwd7PTcFAADc3kp1BsWyrMsuj46OVmpq6hW3U6dOHf3zn/8sza4BAMBthO/iAQAAxiGgAAAA4xBQAACAcQgoAADAOAQUAABgHAIKAAAwDgEFAAAYh4ACAACMQ0ABAADGIaAAAADjEFAAAIBxCCgAAMA4BBQAAGAcAgoAADAOAQUAABiHgAIAAIxDQAEAAMYhoAAAAOMQUAAAgHEIKAAAwDgEFAAAYBwCCgAAMA4BBQAAGIeAAgAAjENAAQAAxiGgAAAA4xBQAACAcQgoAADAOAQUAABgHAIKAAAwDgEFAAAYp1QBZdq0aWrTpo2qV6+usLAw9e3bV+np6V59zp8/r6SkJIWGhiowMFAJCQnKysry6nPs2DHFx8crICBAYWFheuqpp5Sfn3/9RwMAAG4JpQooqampSkpK0vbt25WSkqILFy6oe/fuOnfunN1n9OjRWrt2rVauXKnU1FRlZGSoX79+9vKCggLFx8crLy9P27Zt05IlS7R48WJNnDix7I4KAABUaD6WZVnXuvJ3332nsLAwpaamqmPHjsrJyVGtWrW0bNky9e/fX5L0xRdfqHHjxkpLS1O7du30/vvvq1evXsrIyFB4eLgkad68eRo3bpy+++47+fn5XXG/Ho9HQUFBysnJkdPpvNbyK6S6T79X3iXgJvp6enx5lwAAZaY0n9/XNQYlJydHkhQSEiJJ2rVrly5cuKBu3brZfRo1aqTatWsrLS1NkpSWlqZmzZrZ4USSYmNj5fF4tH///hL3k5ubK4/H4zUBAIBb1zUHlMLCQj355JNq3769mjZtKknKzMyUn5+fgoODvfqGh4crMzPT7vPLcFK0vGhZSaZNm6agoCB7io6OvtayAQBABXDNASUpKUn79u3T8uXLy7KeEo0fP145OTn2dPz48Ru+TwAAUH4qX8tKI0eO1Lp167R161ZFRUXZ7S6XS3l5eTp9+rTXWZSsrCy5XC67z8cff+y1vaK7fIr6XMzhcMjhcFxLqQAAoAIq1RkUy7I0cuRIrVmzRh988IHq1avntbxVq1aqUqWKNm/ebLelp6fr2LFjcrvdkiS32629e/cqOzvb7pOSkiKn06mYmJjrORYAAHCLKNUZlKSkJC1btkzvvPOOqlevbo8ZCQoKkr+/v4KCgjR06FAlJycrJCRETqdTTzzxhNxut9q1aydJ6t69u2JiYvTwww9rxowZyszM1IQJE5SUlMRZEgAAIKmUAWXu3LmSpE6dOnm1L1q0SEOGDJEkzZw5U76+vkpISFBubq5iY2M1Z84cu2+lSpW0bt06jRgxQm63W9WqVVNiYqKmTp16fUcCAABuGdf1HJTywnNQcLvgOSi3F/6+by+349/3TXsOCgAAwI1AQAEAAMYhoAAAAOMQUAAAgHEIKAAAwDgEFAAAYBwCCgAAMA4BBQAAGIeAAgAAjENAAQAAxiGgAAAA4xBQAACAcQgoAADAOAQUAABgHAIKAAAwDgEFAAAYh4ACAACMQ0ABAADGIaAAAADjEFAAAIBxCCgAAMA4BBQAAGAcAgoAADAOAQUAABiHgAIAAIxDQAEAAMYhoAAAAOMQUAAAgHEIKAAAwDgEFAAAYJxSB5StW7eqd+/eioyMlI+Pj95++22v5UOGDJGPj4/X1KNHD68+p06d0qBBg+R0OhUcHKyhQ4fq7Nmz13UgAADg1lHqgHLu3Dm1aNFCs2fPvmSfHj166MSJE/b097//3Wv5oEGDtH//fqWkpGjdunXaunWrhg8fXvrqAQDALalyaVeIi4tTXFzcZfs4HA65XK4Slx08eFDr16/Xzp071bp1a0nSa6+9pp49e+rll19WZGRkaUsCAAC3mBsyBmXLli0KCwvTXXfdpREjRujkyZP2srS0NAUHB9vhRJK6desmX19f7dixo8Tt5ebmyuPxeE0AAODWVeYBpUePHnrzzTe1efNmvfjii0pNTVVcXJwKCgokSZmZmQoLC/Nap3LlygoJCVFmZmaJ25w2bZqCgoLsKTo6uqzLBgAABin1JZ4reeihh+zXzZo1U/PmzXXHHXdoy5Yt6tq16zVtc/z48UpOTrbnPR4PIQUAgFvYDb/NuH79+qpZs6YOHTokSXK5XMrOzvbqk5+fr1OnTl1y3IrD4ZDT6fSaAADAreuGB5RvvvlGJ0+eVEREhCTJ7Xbr9OnT2rVrl93ngw8+UGFhodq2bXujywEAABVAqS/xnD171j4bIklHjhzR7t27FRISopCQEE2ZMkUJCQlyuVw6fPiwxo4dqwYNGig2NlaS1LhxY/Xo0UPDhg3TvHnzdOHCBY0cOVIPPfQQd/AAAABJ13AG5ZNPPtHdd9+tu+++W5KUnJysu+++WxMnTlSlSpW0Z88e/frXv9add96poUOHqlWrVvrf//1fORwOextLly5Vo0aN1LVrV/Xs2VMdOnTQggULyu6oAABAhVbqMyidOnWSZVmXXL5hw4YrbiMkJETLli0r7a4BAMBtgu/iAQAAxiGgAAAA4xBQAACAcQgoAADAOAQUAABgHAIKAAAwDgEFAAAYh4ACAACMQ0ABAADGIaAAAADjEFAAAIBxCCgAAMA4BBQAAGAcAgoAADAOAQUAABiHgAIAAIxDQAEAAMYhoAAAAOMQUAAAgHEIKAAAwDgEFAAAYBwCCgAAMA4BBQAAGIeAAgAAjENAAQAAxiGgAAAA4xBQAACAcQgoAADAOAQUAABgHAIKAAAwDgEFAAAYp9QBZevWrerdu7ciIyPl4+Ojt99+22u5ZVmaOHGiIiIi5O/vr27duunLL7/06nPq1CkNGjRITqdTwcHBGjp0qM6ePXtdBwIAAG4dpQ4o586dU4sWLTR79uwSl8+YMUOvvvqq5s2bpx07dqhatWqKjY3V+fPn7T6DBg3S/v37lZKSonXr1mnr1q0aPnz4tR8FAAC4pVQu7QpxcXGKi4srcZllWZo1a5YmTJigPn36SJLefPNNhYeH6+2339ZDDz2kgwcPav369dq5c6dat24tSXrttdfUs2dPvfzyy4qMjLyOwwEAALeCMh2DcuTIEWVmZqpbt252W1BQkNq2bau0tDRJUlpamoKDg+1wIkndunWTr6+vduzYUeJ2c3Nz5fF4vCYAAHDrKtOAkpmZKUkKDw/3ag8PD7eXZWZmKiwszGt55cqVFRISYve52LRp0xQUFGRP0dHRZVk2AAAwTIW4i2f8+PHKycmxp+PHj5d3SQAA4AYq04DicrkkSVlZWV7tWVlZ9jKXy6Xs7Gyv5fn5+Tp16pTd52IOh0NOp9NrAgAAt64yDSj16tWTy+XS5s2b7TaPx6MdO3bI7XZLktxut06fPq1du3bZfT744AMVFhaqbdu2ZVkOAACooEp9F8/Zs2d16NAhe/7IkSPavXu3QkJCVLt2bT355JP6y1/+ooYNG6pevXp69tlnFRkZqb59+0qSGjdurB49emjYsGGaN2+eLly4oJEjR+qhhx7iDh4AACDpGgLKJ598os6dO9vzycnJkqTExEQtXrxYY8eO1blz5zR8+HCdPn1aHTp00Pr161W1alV7naVLl2rkyJHq2rWrfH19lZCQoFdffbUMDgcAANwKfCzLssq7iNLyeDwKCgpSTk7ObTcepe7T75V3CbiJvp4eX94l4Cbi7/v2cjv+fZfm87tC3MUDAABuLwQUAABgHAIKAAAwDgEFAAAYh4ACAACMQ0ABAADGIaAAAADjEFAAAIBxCCgAAMA4BBQAAGAcAgoAADAOAQUAABiHgAIAAIxDQAEAAMYhoAAAAOMQUAAAgHEIKAAAwDgEFAAAYBwCCgAAMA4BBQAAGIeAAgAAjENAAQAAxiGgAAAA4xBQAACAcQgoAADAOAQUAABgHAIKAAAwDgEFAAAYh4ACAACMQ0ABAADGIaAAAADjlHlAmTx5snx8fLymRo0a2cvPnz+vpKQkhYaGKjAwUAkJCcrKyirrMgAAQAV2Q86gNGnSRCdOnLCnf/3rX/ay0aNHa+3atVq5cqVSU1OVkZGhfv363YgyAABABVX5hmy0cmW5XK5i7Tk5Ofrb3/6mZcuWqUuXLpKkRYsWqXHjxtq+fbvatWt3I8oBAAAVzA05g/Lll18qMjJS9evX16BBg3Ts2DFJ0q5du3ThwgV169bN7tuoUSPVrl1baWlpl9xebm6uPB6P1wQAAG5dZR5Q2rZtq8WLF2v9+vWaO3eujhw5onvvvVdnzpxRZmam/Pz8FBwc7LVOeHi4MjMzL7nNadOmKSgoyJ6io6PLumwAAGCQMr/EExcXZ79u3ry52rZtqzp16ugf//iH/P39r2mb48ePV3Jysj3v8XgIKQAA3MJu+G3GwcHBuvPOO3Xo0CG5XC7l5eXp9OnTXn2ysrJKHLNSxOFwyOl0ek0AAODWdcMDytmzZ3X48GFFRESoVatWqlKlijZv3mwvT09P17Fjx+R2u290KQAAoIIo80s8Y8aMUe/evVWnTh1lZGRo0qRJqlSpkgYOHKigoCANHTpUycnJCgkJkdPp1BNPPCG3280dPAAAwFbmAeWbb77RwIEDdfLkSdWqVUsdOnTQ9u3bVatWLUnSzJkz5evrq4SEBOXm5io2NlZz5swp6zIAAEAFVuYBZfny5ZddXrVqVc2ePVuzZ88u610DAIBbBN/FAwAAjENAAQAAxiGgAAAA4xBQAACAcQgoAADAOAQUAABgHAIKAAAwDgEFAAAYh4ACAACMQ0ABAADGIaAAAADjEFAAAIBxCCgAAMA4BBQAAGAcAgoAADAOAQUAABiHgAIAAIxDQAEAAMYhoAAAAOMQUAAAgHEIKAAAwDgEFAAAYBwCCgAAMA4BBQAAGIeAAgAAjENAAQAAxiGgAAAA4xBQAACAcQgoAADAOAQUAABgnHINKLNnz1bdunVVtWpVtW3bVh9//HF5lgMAAAxRbgFlxYoVSk5O1qRJk/Tpp5+qRYsWio2NVXZ2dnmVBAAADFFuAeWvf/2rhg0bpkceeUQxMTGaN2+eAgIC9MYbb5RXSQAAwBCVy2OneXl52rVrl8aPH2+3+fr6qlu3bkpLSyvWPzc3V7m5ufZ8Tk6OJMnj8dz4Yg1TmPtjeZeAm+h2/B2/nfH3fXu5Hf++i47Zsqwr9i2XgPL999+roKBA4eHhXu3h4eH64osvivWfNm2apkyZUqw9Ojr6htUImCBoVnlXAOBGuZ3/vs+cOaOgoKDL9imXgFJa48ePV3Jysj1fWFioU6dOKTQ0VD4+PuVYGW4Gj8ej6OhoHT9+XE6ns7zLAVCG+Pu+vViWpTNnzigyMvKKfcsloNSsWVOVKlVSVlaWV3tWVpZcLlex/g6HQw6Hw6stODj4RpYIAzmdTv4BA25R/H3fPq505qRIuQyS9fPzU6tWrbR582a7rbCwUJs3b5bb7S6PkgAAgEHK7RJPcnKyEhMT1bp1a91zzz2aNWuWzp07p0ceeaS8SgIAAIYot4AyYMAAfffdd5o4caIyMzPVsmVLrV+/vtjAWcDhcGjSpEnFLvMBqPj4+8al+FhXc68PAADATcR38QAAAOMQUAAAgHEIKAAAwDgEFBgjIyOjvEsAABiCgAJjNGnSRMuWLSvvMgAABiCgwBjPP/+8Hn30UT3wwAM6depUeZcDAChHBBQY4/HHH9eePXt08uRJxcTEaO3ateVdEgCgnPAcFBjp9ddf1+jRo9W4cWNVruz9PMFPP/20nKoCcD18fX2v+AWvPj4+ys/Pv0kVwWQV4tuMcXs5evSoVq9erRo1aqhPnz7FAgqAimnNmjWXXJaWlqZXX31VhYWFN7EimIx/+WGUhQsX6k9/+pO6deum/fv3q1atWuVdEoAy0qdPn2Jt6enpevrpp7V27VoNGjRIU6dOLYfKYCICCozRo0cPffzxx3r99dc1ePDg8i4HwA2UkZGhSZMmacmSJYqNjdXu3bvVtGnT8i4LBiGgwBgFBQXas2ePoqKiyrsUADdITk6OXnjhBb322mtq2bKlNm/erHvvvbe8y4KBGCQLALgpZsyYoRdffFEul0svvPBCiZd8gCIEFADATeHr6yt/f39169ZNlSpVumS/1atX38SqYCou8QAAborBgwdf8TZjoAhnUAAAgHF4kiwAADAOAQUAABiHgAIAAIxDQAEAAMYhoAAAAOMQUIDbzJAhQ9S3b9/yLuOSFi5cqBYtWigwMFDBwcG6++67NW3aNHv5tdY/efJktWzZsuwKBXBD8RwUAMZ444039OSTT+rVV1/Vfffdp9zcXO3Zs0f79u0r79IA3GScQQFgS01N1T333COHw6GIiAg9/fTTys/Pt5evX79eHTp0UHBwsEJDQ9WrVy8dPnzYXv7111/Lx8dHq1evVufOnRUQEKAWLVooLS3tqvb/7rvv6sEHH9TQoUPVoEEDNWnSRAMHDtTzzz8v6eezIEuWLNE777wjHx8f+fj4aMuWLZKkcePG6c4771RAQIDq16+vZ599VhcuXJAkLV68WFOmTNHnn39ur7d48WK73t27d9s1nD592mu7P/zwgwYNGqRatWrJ399fDRs21KJFi67jXQZwNTiDAkCS9O2336pnz54aMmSI3nzzTX3xxRcaNmyYqlatqsmTJ0uSzp07p+TkZDVv3lxnz57VxIkT9Zvf/Ea7d++Wr+///f/OM888o5dfflkNGzbUM888o4EDB+rQoUOqXPny/+S4XC6lpqbq6NGjqlOnTrHlY8aM0cGDB+XxeOyQEBISIkmqXr26Fi9erMjISO3du1fDhg1T9erVNXbsWA0YMED79u3T+vXrtWnTJklSUFCQsrKyrvi+PPvsszpw4IDef/991axZU4cOHdJPP/10Ve8pgGtHQAEgSZozZ46io6P1+uuvy8fHR40aNVJGRobGjRuniRMnytfXVwkJCV7rvPHGG6pVq5YOHDigpk2b2u1jxoxRfHy8JGnKlClq0qSJDh06pEaNGl22hkmTJqlfv36qW7eu7rzzTrndbvXs2VP9+/eXr6+vAgMD5e/vr9zcXLlcLq91J0yYYL+uW7euxowZo+XLl2vs2LHy9/dXYGCgKleuXGy9Kzl27JjuvvtutW7d2t42gBuPSzwAJEkHDx6U2+32+q6U9u3b6+zZs/rmm28kSV9++aUGDhyo+vXry+l02h/Wx44d89pW8+bN7dcRERGSpOzs7CvWEBERobS0NO3du1ejRo1Sfn6+EhMT1aNHDxUWFl523RUrVqh9+/ZyuVwKDAzUhAkTitV1LUaMGKHly5erZcuWGjt2rLZt23bd2wRwZQQUAFetd+/eOnXqlBYuXKgdO3Zox44dkqS8vDyvflWqVLFfFwWeKwWMX2ratKkef/xxvfXWW0pJSVFKSopSU1Mv2T8tLU2DBg1Sz549tW7dOn322Wd65plnitV1saLLUr/8SrKicStF4uLidPToUY0ePVoZGRnq2rWrxowZc9XHAuDaEFAASJIaN26stLQ0rw/rjz76SNWrV1dUVJROnjyp9PR0TZgwQV27dlXjxo31ww8/3PC6YmJiJP08/kWS/Pz8VFBQ4NVn27ZtqlOnjp555hm1bt1aDRs21NGjR736lLRerVq1JEknTpyw2345YPaX/RITE/XWW29p1qxZWrBgwXUfF4DLYwwKcBvKyckp9kE8fPhwzZo1S0888YRGjhyp9PR0TZo0ScnJyfL19VWNGjUUGhqqBQsWKCIiQseOHdPTTz9dpnWNGDFCkZGR6tKli6KionTixAn95S9/Ua1ateR2uyX9PAZkw4YNSk9PV2hoqIKCgtSwYUMdO3ZMy5cvV5s2bfTee+9pzZo1XtuuW7eujhw5ot27dysqKkrVq1eXv7+/2rVrp+nTp6tevXrKzs72GssiSRMnTlSrVq3UpEkT5ebmat26dWrcuHGZHjeAElgAbiuJiYmWpGLT0KFDrS1btlht2rSx/Pz8LJfLZY0bN866cOGCvW5KSorVuHFjy+FwWM2bN7e2bNliSbLWrFljWZZlHTlyxJJkffbZZ/Y6P/zwgyXJ+vDDD69Y26pVq6yePXtaERERlp+fnxUZGWklJCRYe/bssftkZ2db999/vxUYGOi13aeeesoKDQ21AgMDrQEDBlgzZ860goKC7PXOnz9vJSQkWMHBwZYka9GiRZZlWdaBAwcst9tt+fv7Wy1btrQ2btzotd3nnnvOaty4seXv72+FhIRYffr0sb766qtreesBlIKPZf3ifC4AAIABGIMCAACMQ0ABcNPExcUpMDCwxOmFF14o7/IAGIRLPABumm+//faST2ENCQmxnwoLAAQUAABgHC7xAAAA4xBQAACAcQgoAADAOAQUAABgHAIKAAAwDgEFAAAYh4ACAACM8/8ArrW6ViGzwYoAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **STEP 6 — Education Distribution**"
      ],
      "metadata": {
        "id": "PZ9CZWGqrH4F"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df['Education'].value_counts().plot(\n",
        "    kind='bar'\n",
        ")\n",
        "\n",
        "plt.title(\n",
        "    'Education Distribution'\n",
        ")\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 552
        },
        "id": "C_XnuEk0rOrS",
        "outputId": "bd092710-a539-4997-98a4-04ff34bc4390"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAigAAAIXCAYAAAC2IaX9AAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAOlJJREFUeJzt3Xl4FFW+xvG3s3RWOiFMFrjsmxAW2QYIIiBEAkYGBOeODIMBUREJOCCK3EGQDAybIqACznhZXBDUERUQNEaEAQIjYRlEQJZg0CwgkYSwJCSp+4dP+tIElEBIn+D38zz1POlzTnf9Kkknb1edqrJZlmUJAADAIB7uLgAAAOByBBQAAGAcAgoAADAOAQUAABiHgAIAAIxDQAEAAMYhoAAAAOMQUAAAgHEIKAAAwDgEFKCCHDt2TDabTUuXLnV3KVf1xRdfyGaz6YsvvnB3Kdekbt26GjJkyE1fz5V+dkOGDFFgYOBNX3cJm82m5557rsLWB7gbAQW4RkuXLpXNZrvqsm3bNneXeM0WLFhgXFDq1q2b83vp4eEhh8Oh2267TYMHD1ZiYmK5refjjz829h+9ybUBFc3L3QUAlU1CQoLq1atXqr1hw4ZuqOb6LFiwQL/5zW9K7X3o0qWLzp8/L7vd7pa6atasqenTp0uSzp49q8OHD+v999/Xm2++qf/+7//Wm2++KW9vb+f4gwcPysOjbJ+zPv74Y73yyitlCgJ16tTR+fPnXdZ9M/xcbefPn5eXF3+y8evBbztQRr1791a7du3cXcZN4eHhIV9fX7etPygoSH/6059c2mbMmKHRo0drwYIFqlu3rmbOnOns8/Hxuan1FBYWqri4WHa73a3fF0luXz9Q0TjEA9wEp0+f1pAhQxQUFKTg4GDFxcXp9OnTpcZ169ZN3bp1K9U+ZMgQ1a1b16WtuLhY8+bNU4sWLeTr66vQ0FD16tVLO3bscI5ZsmSJunfvrrCwMPn4+CgyMlILFy50eZ26detq37592rhxo/OQSkkNV5uD8u6776pt27by8/PTb37zG/3pT3/S999/X6rmwMBAff/99+rXr58CAwMVGhqqcePGqaio6Jq/d5fz9PTU/PnzFRkZqZdfflk5OTku23LpXqCLFy9qypQpatSokXx9fVWtWjV17tzZeYhoyJAheuWVVyTJ5fCc9P/zTJ5//nnNnTtXDRo0kI+Pj77++uufnT909OhRxcTEKCAgQDVq1FBCQoIuvUn81b6nl7/mz9VW0nb5npVdu3apd+/ecjgcCgwMVI8ePUodaiw5NLllyxaNHTtWoaGhCggI0H333aeTJ0/+8g8AcBP2oABllJOTox9++MGlzWazqVq1apIky7LUt29fbd68WY899piaNm2qVatWKS4u7obWO2zYMC1dulS9e/fWww8/rMLCQv3rX//Stm3bnHt0Fi5cqGbNmul3v/udvLy8tHr1aj3++OMqLi7WyJEjJUlz587VqFGjFBgYqL/85S+SpPDw8Kuud+nSpRo6dKh++9vfavr06crKytK8efO0ZcsW7dq1S8HBwc6xRUVFiomJUYcOHfT888/rs88+0wsvvKAGDRpoxIgR173tnp6eGjhwoJ599llt3rxZsbGxVxz33HPPafr06Xr44YfVvn175ebmaseOHdq5c6fuvvtuDR8+XOnp6UpMTNQbb7xxxddYsmSJLly4oEcffVQ+Pj4KCQlRcXHxFccWFRWpV69e6tixo2bNmqX169dr8uTJKiwsVEJCQpm28Vpqu9S+fft05513yuFw6Omnn5a3t7deffVVdevWTRs3blSHDh1cxo8aNUpVq1bV5MmTdezYMc2dO1fx8fFauXJlmeoEKowF4JosWbLEknTFxcfHxznugw8+sCRZs2bNcrYVFhZad955pyXJWrJkibO9a9euVteuXUutKy4uzqpTp47z8eeff25JskaPHl1qbHFxsfPrc+fOleqPiYmx6tev79LWrFmzK653w4YNliRrw4YNlmVZVkFBgRUWFmY1b97cOn/+vHPcmjVrLEnWpEmTXGqWZCUkJLi8ZuvWra22bduWWtflunbtajVr1uyq/atWrbIkWfPmzXO21alTx4qLi3M+vv32263Y2NifXc/IkSOtK/3pS01NtSRZDofDOnHixBX7Lv3ZlWzvqFGjnG3FxcVWbGysZbfbrZMnT1qWVfp7+nOvebXaLMuyJFmTJ092Pu7Xr59lt9utI0eOONvS09OtKlWqWF26dHG2lfzeRkdHu/yujBkzxvL09LROnz59xfUB7sYhHqCMXnnlFSUmJros69atc/Z//PHH8vLyctlj4OnpqVGjRl33Ov/5z3/KZrNp8uTJpfouPQzg5+fn/LpkT0/Xrl119OhRl0Mj12rHjh06ceKEHn/8cZc5ELGxsWrSpInWrl1b6jmPPfaYy+M777xTR48eLfO6L1dySu+ZM2euOiY4OFj79u3ToUOHrns9AwYMUGho6DWPj4+Pd35ts9kUHx+vgoICffbZZ9ddwy8pKirSp59+qn79+ql+/frO9urVq+uPf/yjNm/erNzcXJfnPProoy6/K3feeaeKior07bff3rQ6gRvBIR6gjNq3b/+zk2S//fZbVa9evdQ1Mm677bbrXueRI0dUo0YNhYSE/Oy4LVu2aPLkyUpOTta5c+dc+nJychQUFFSm9Zb887pS7U2aNNHmzZtd2krmxlyqatWq+vHHH8u03ivJy8uTJFWpUuWqYxISEtS3b181btxYzZs3V69evTR48GC1bNnymtdzpTO0rsbDw8MlIEhS48aNJf00x+RmOXnypM6dO3fFn0vTpk1VXFys48ePq1mzZs722rVru4yrWrWqJJXLzwa4GdiDArjRpZ9oL3U9k0qPHDmiHj166IcfftCcOXO0du1aJSYmasyYMZJ01XkU5cnT0/OmvfZXX30l6edP5+7SpYuOHDmixYsXq3nz5nrttdfUpk0bvfbaa9e8nkv3QpWH8vwZ34ir/WysSyb0AiYhoADlrE6dOsrIyHB+4i9x8ODBUmOrVq16xbN7Lt/t3qBBA6Wnpys7O/uq6129erXy8/P10Ucfafjw4brnnnsUHR19xX+4V/uneaVtuVrtBw8edPbfbEVFRVq+fLn8/f3VuXPnnx0bEhKioUOH6u2339bx48fVsmVLl7NfrnXbr0VxcXGpw1fffPONJDnPwirZU3H5z/lKh1autbbQ0FD5+/tf8edy4MABeXh4qFatWtf0WoCpCChAObvnnntUWFjocnpvUVGRXnrppVJjGzRooAMHDric7rlnzx5t2bLFZdyAAQNkWZamTJlS6jVKPgGXfEK+9BNxTk6OlixZUuo5AQEBVwxGl2vXrp3CwsK0aNEi5efnO9vXrVun/fv3X/VsmvJUVFSk0aNHa//+/Ro9erQcDsdVx546dcrlcWBgoBo2bOhSe0BAgKTSgeF6vfzyy86vLcvSyy+/LG9vb/Xo0UPSTyHP09NTmzZtcnneggULSr3Wtdbm6empnj176sMPP3Q5lJSVlaXly5erc+fOP/t9AioD5qAAZbRu3TodOHCgVHunTp1Uv3599enTR3fccYeeeeYZHTt2TJGRkXr//fevOEn1oYce0pw5cxQTE6Nhw4bpxIkTWrRokZo1a+YyyfGuu+7S4MGDNX/+fB06dEi9evVScXGx/vWvf+muu+5SfHy8evbsKbvdrj59+mj48OHKy8vTP/7xD4WFhSkjI8NlvW3bttXChQs1depUNWzYUGFhYerevXup+ry9vTVz5kwNHTpUXbt21cCBA52nGdetW9d5+Ki85OTk6M0335QknTt3znkl2SNHjuiBBx7QX//61599fmRkpLp166a2bdsqJCREO3bs0HvvvecykbVt27aSpNGjRysmJkaenp564IEHrqteX19frV+/XnFxcerQoYPWrVuntWvX6n/+53+cc3GCgoL0+9//Xi+99JJsNpsaNGigNWvW6MSJE6Veryy1TZ06VYmJiercubMef/xxeXl56dVXX1V+fr5mzZp1XdsDGMWt5xABlcjPnWasy04XPXXqlDV48GDL4XBYQUFB1uDBg61du3aVGmdZlvXmm29a9evXt+x2u9WqVSvrk08+KXWasWX9dKry7NmzrSZNmlh2u90KDQ21evfubaWkpDjHfPTRR1bLli0tX19fq27dutbMmTOtxYsXW5Ks1NRU57jMzEwrNjbWqlKliiXJecrx1U6JXblypdW6dWvLx8fHCgkJsQYNGmR99913LmPi4uKsgICAUt+3yZMnX/XU2Ut17drV5fsZGBhoNWrUyPrTn/5kffrpp1d8zuWnGU+dOtVq3769FRwcbPn5+VlNmjSxpk2bZhUUFLh8H0eNGmWFhoZaNpvNWVvJab+zZ88utZ6rnWYcEBBgHTlyxOrZs6fl7+9vhYeHW5MnT7aKiopcnn/y5ElrwIABlr+/v1W1alVr+PDh1ldffVXqNa9Wm2WVPs3Ysixr586dVkxMjBUYGGj5+/tbd911l7V161aXMSW/t19++aVL+9V+1oApbJbFDCkAAGAW5qAAAADjEFAAAIBxCCgAAMA4BBQAAGAcAgoAADAOAQUAABinTBdqe+6550pdyfK2225zXrTqwoULevLJJ7VixQrl5+crJiZGCxYsUHh4uHN8WlqaRowYoQ0bNigwMFBxcXGaPn26vLyuvZTi4mKlp6erSpUq5XrZagAAcPNYlqUzZ86oRo0a8vD4+X0kZb6SbLNmzVxuI35psBgzZozWrl2rd999V0FBQYqPj1f//v2dl+0u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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **STEP 7 — Property Area Distribution**"
      ],
      "metadata": {
        "id": "W_Xf-FZ_sa3i"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df['Property_Area'].value_counts().plot(\n",
        "    kind='bar'\n",
        ")\n",
        "\n",
        "plt.title(\n",
        "    'Property Area Distribution'\n",
        ")\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 533
        },
        "id": "xDUTAY84sdxa",
        "outputId": "4ccf3f79-2423-4553-ec04-261826b6d7ab"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAigAAAIECAYAAAAzY9XIAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAOXNJREFUeJzt3XlYFvX+//HXDQgICIiyiCvuWqYeLSWXXEjcM6nUzMBMzzGXcqm0/Lp10jLTjsfteDLNLU9aaWnminJyKVPLUnNFsRQ1F3A5gsD8/vDi/nUHKhp4f+R+Pq5rrqv5zGdm3nMzyYuZz9xjsyzLEgAAgEHcnF0AAADAHxFQAACAcQgoAADAOAQUAABgHAIKAAAwDgEFAAAYh4ACAACMQ0ABAADGIaAAAADjEFAAuKSNGzfKZrNp48aNBb6v0aNHy2azObTZbDb179+/wPctSXPnzpXNZtPRo0fvyv6A/EBAgcvI/kc6e/L29lbVqlXVv39/nTp1ytnl3bG9e/dq9OjRBfrL56mnnpLNZtOrr75aYPv4M44ePerwsy1SpIhKliyphx9+WK+99pqSkpLybV/jxo3TsmXL8m17+cnk2oDbZeNdPHAVc+fOVc+ePTV27FhFRETo6tWr+vrrrzV//nyVL19eP/30k3x8fJxd5m1bunSpnnzyScXHx6tZs2b5vv3U1FSFhoYqLCxMmZmZOnbsWI6rAc529OhRRUREqFu3bmrbtq2ysrJ0/vx5bd++XZ9++qlsNptmz56trl272tfJyspSenq6PD095eaW97/V/Pz89MQTT2ju3Ll5XicjI0MZGRny9va2t9lsNvXr109Tp07N83butLbMzExdu3ZNXl5exv3sgBvxcHYBwN3Wpk0b1a9fX5L0/PPPq0SJEpo0aZKWL1+ubt265brO5cuX5evrezfLvKWrV6/K09OzwPfzySefKDMzUx988IFatGihhIQEPfLII7dczxmf2V/+8hc988wzDm3Hjh1Tq1atFBsbqxo1aqh27dqSJDc3N4fAUBCyPwMPDw95eDjvn1t3d3e5u7s7bf/AneAWD1xeixYtJEmJiYmSpLi4OPn5+enw4cNq27atihUrpu7du0u6/gtnyJAhKlu2rLy8vFStWjVNnDhRf7wQmT2+YOHChapWrZq8vb1Vr149JSQk5Nj/r7/+queee06hoaHy8vLSfffdpw8++MChT/Z4icWLF2vEiBEqXbq0fHx8NGXKFD355JOSpObNm9tvcWzcuFGxsbEqWbKkrl27lmOfrVq1UrVq1fL0+SxcuFCPPvqomjdvrho1amjhwoU5+mTfPtu0aZNeeOEFhYSEqEyZMvblq1atUpMmTeTr66tixYqpXbt22rNnj8M2du/erbi4OFWsWFHe3t4KCwvTc889p7Nnz+apzhspX7685s6dq/T0dE2YMMHentsYlIMHDyomJkZhYWHy9vZWmTJl1LVrV6WkpEi6/nO9fPmyPvzwQ/tnHRcXJ+n/jzPZu3evnn76aRUvXlyNGzd2WJabW50jcXFxqlChQo71/rjNm9V2ozEo06dP13333ScvLy+Fh4erX79+unDhgkOfZs2a6f7779fevXvVvHlz+fj4qHTp0g6fJVAQuIICl3f48GFJUokSJextGRkZio6OVuPGjTVx4kT5+PjIsix17NhR8fHx6tWrl+rUqaPVq1fr5Zdf1q+//qrJkyc7bHfTpk36z3/+o4EDB8rLy0vTp09X69at9e233+r++++XJJ06dUoNGza0B5rg4GCtWrVKvXr1Umpqql566SWHbb7xxhvy9PTU0KFDlZaWplatWmngwIGaMmWKXnvtNdWoUUOSVKNGDfXo0UPz5s3T6tWr1b59e/s2kpOTtWHDBo0aNeqWn82JEycUHx+vDz/8UJLUrVs3TZ48WVOnTs316s0LL7yg4OBgjRw5UpcvX5YkzZ8/X7GxsYqOjtbbb7+tK1euaMaMGWrcuLF27dpl/+W7du1aHTlyRD179lRYWJj27NmjWbNmac+ePdq2bdufujURGRmpSpUqae3atTfsk56erujoaKWlpWnAgAEKCwvTr7/+qhUrVujChQsKCAjQ/Pnz9fzzz+uhhx5Snz59JEmVKlVy2M6TTz6pKlWqaNy4cTmC6x/l5RzJq7zU9nujR4/WmDFjFBUVpb59+2r//v2aMWOGtm/frs2bN6tIkSL2vufPn1fr1q3VuXNnPfXUU1q6dKleffVV1apVS23atLmtOoE8swAXMWfOHEuStW7dOuvMmTPW8ePHrcWLF1slSpSwihYtav3yyy+WZVlWbGysJckaNmyYw/rLli2zJFl///vfHdqfeOIJy2azWYcOHbK3SbIkWd9995297dixY5a3t7f1+OOP29t69epllSpV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317r1q1zdlkAnIQrKC4oICBAixcvVps2bRzav/zyS3Xr1k0pKSlOqgyuavr06XrxxRf1xBNPKDIyUpK0bds2LV26VJMnT+bFbHCKsWPH3nT5yJEj71IlromA4oJCQkK0adMm1ahRw6F93759atq0qc6cOeOkyuCqypQpo2HDhql///4O7dOmTdO4ceP066+/OqkyuLK6des6zF+7dk2JiYny8PBQpUqVtHPnTidV5hoIKC5o7Nix+vnnnzVnzhx5eXlJktLS0tSrVy9VqVJFo0aNcnKFcDV+fn76/vvvVblyZYf2gwcPqm7duvaxUoCzpaamKi4uTo8//rh69Ojh7HIKNQKKi+jcubPD/Lp16+Tl5aXatWtLkn744Qelp6erZcuW+vTTT51RIlzY008/rbp16+rll192aJ84caK+++47LV682EmVATn9+OOP6tChg44ePersUgo13mbsIgICAhzmY2JiHOZ5zBh32++/FLBmzZp68803tXHjRocxKJs3b9aQIUOcVSKQq5SUFMbq3QVcQXExlmXp+PHjCg4OVtGiRZ1dDlxYREREnvrZbDYdOXKkgKsBcvrjN2tblqWTJ09q/vz5atq0qT766CMnVeYaCCguJisrS97e3tqzZ4+qVKni7HIAwFh/DNFubm4KDg5WixYtNHz4cBUrVsxJlbkGvgfFxbi5ualKlSo6e/ass0sBJF1/MqJSpUrat2+fs0sBHCQmJjpMhw8f1saNG1WiRAn+wLsLCCgu6K233tLLL7+sn376ydmlACpSpIiuXr3q7DIAu7S0NA0fPlz169dXo0aNtGzZMknSnDlzVKlSJf3jH//QoEGDnFukC+AWjwsqXry4rly5ooyMDHl6euYYi5L9qnvgbhk3bpwOHDig999/Xx4ejN2Hc7366qv617/+paioKG3ZskVnzpxRz549tW3bNr322mt68skn5e7u7uwyCz3+JXBB7733nrNLABxs375d69ev15o1a1SrVq0cb43l0XfcTUuWLNG8efPUsWNH/fTTT3rggQeUkZGhH374gTe+30VcQQHgdD179rzp8jlz5tylSgDJ09NTiYmJKl26tCSpaNGi+vbbb1WrVi0nV+ZauILigpKSkm66vFy5cnepEuA6AghMkpmZKU9PT/u8h4eH/Pz8nFiRa+IKigtyc3O76WXKzMzMu1gNXFnx4sVz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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **STEP 8 — Boxplot for Income**"
      ],
      "metadata": {
        "id": "wJvUgQz2tFl9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(8,5))\n",
        "\n",
        "plt.boxplot(\n",
        "    df['ApplicantIncome']\n",
        ")\n",
        "\n",
        "plt.title(\n",
        "    'Applicant Income Boxplot'\n",
        ")\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 468
        },
        "id": "ruiYJRxLtEbH",
        "outputId": "2b9f10f2-aa23-4d18-a19b-c54f480afde1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x500 with 1 Axes>"
            ],
            "image/png": "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sfbu3avhw4fL5XJ51F/s1RVOdzzzKzfNXYhj/lov7u/q3nvvVXp6eq2111xzzVn15A6ha9as0cMPP1znzx86dEgbNmyQJH399ddyuVw1ZrbPFQ9kAC4NhFoAdbJgwQK1adNGM2fOrDGWnZ2tDz74QHPmzPH4035hYWGN2m+++UYREREe21wul77//ntrdtZdJ6lG7S+56qqrJElbt2497dq5W7Zs0TfffKP58+frvvvus7bn5uae8XF+7mKGm6uuukoul0tff/21evToUWtNhw4dJEk7d+70mAGvqqpSUVGREhMTz0svrVu3VtOmTVVdXX3e9ul28uRJSdJPP/0kyfOcfm7Hjh1q1aqVGjdubG0bM2aMKioqlJWVpczMTL366qs1LheQzvx39FQdOnSQy+VSYWGhOnfubG0vLS1VWVmZ1atE8AUuBi4/AHDGjh07puzsbN1+++1KS0ur8Ro7dqwqKir04YcfenxuyZIl2rt3r/V+/fr1WrdunW699dYax5gxY4b1szFGM2bMUMOGDU/7Z+PaDBgwQE2bNlVWVpaOHz/uMeaeXXTPPp4682mM0fTp08/4OD8XFBQkSTWWy7oQUlJS5Ovrq2effbbGrLL7nBITE+Xv76/XXnvN4zz/8pe/qLy8XMnJyeelFz8/Pw0cOFDvv/9+rctgHThw4Kz3/dFHH0mSunfvLklq27atevToofnz53t8z1u3btXf//533Xbbbda2xYsXa+HChXrhhRc0YcIEDR48WE8//bT1f5ROVZffUTf3sV599VWP7X/6058kyeP7bdy48UX5vQAuZ8zUAjhjH374oSoqKvTb3/621vG+ffuqdevWWrBggQYNGmRtj4qK0g033KDRo0ersrJSr776qlq2bKknnnjC4/ONGjXSsmXLlJ6ertjYWH3yySdaunSpnnrqqRrXs/4Sh8OhV155RaNGjVLv3r01dOhQNW/eXJs3b9bRo0c1f/58RUdH66qrrtJjjz2mvXv3yuFw6P333z+na2QDAwPVpUsXLVy4UJ06dVKLFi3UrVu3X72292xERUXp97//vf7whz8oPj5eqampCggI0JdffqmwsDBlZWWpdevWyszM1JQpU3TLLbfot7/9rXbu3KlZs2apd+/eHg86OFcvvPCCPvvsM8XGxuqBBx5Qly5ddPjwYW3cuFGffvrpGT3qdu/evXr7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KSnJqhk0aJAOHDigiRMnqqSkRD169NCyZctq3DwGAACAy8M5rVNrd6xTCwAAcGm74OvUAgAAAJcKQi0AAABsj1ALAAAA2yPUAgAAwPYItQAAALA9Qi0AAABsj1ALAAAA2yPUAgAAwPYItQAAALA9Qi0AAABsj1ALAAAA2yPUAgAAwPYItQAAALA9Qi0AAABsj1ALAAAA2yPUAgAAwPYItQAAALC9Bt5uAABwflRXVysvL0/FxcVq27at4uPj5efn5+22AOCiYKYWAOqB7OxsRUVFKSEhQUOHDlVCQoKioqKUnZ3t7dYA4KIg1AKAzWVnZystLU0xMTHKz89XRUWF8vPzFRMTo7S0NIItgMuCjzHGeLsJb3E6nQoODlZ5ebkcDoe32wGAOquurlZUVJRiYmK0ZMkS+fr+Z67C5XIpJSVFW7duVWFhIZciALClM81rzNQCgI3l5eVp165deuqppzwCrST5+voqMzNTRUVFysvL81KHAHBxEGoBwMaKi4slSd26dat13L3dXQcA9RWhFgBsrG3btpKkrVu31jru3u6uA4D6ilALADYWHx+viIgIPf/883K5XB5jLpdLWVlZioyMVHx8vJc6BICLg1ALADbm5+enadOmKScnRykpKR6rH6SkpCgnJ0cvv/wyN4kBqPd4+AIA2FxqaqoWL16sRx99VP369bO2R0ZGavHixUpNTfVidwBwcbCkF0t6AagneKIYgProTPMaM7UAUE/4+fnppptu8nYbAOAVXFMLAAAA2yPUAgAAwPYItQAAALC9OofavXv36t5771XLli0VGBiomJgYbdiwwRo3xmjixIlq27atAgMDlZiYqMLCQo99HD58WPfcc48cDoeaNWumkSNH6qeffvKo+eqrrxQfH69GjRopPDxcU6dOrdHLokWLFB0drUaNGikmJkYff/xxXU8HAAAA9UCdQu2PP/6o66+/Xg0bNtQnn3yir7/+WtOmTVPz5s2tmqlTp+q1117TnDlztG7dOjVu3FhJSUk6fvy4VXPPPfdo27Ztys3NVU5OjtasWaMHH3zQGnc6nRowYIA6dOiggoICvfTSS5o8ebLmzp1r1axdu1ZDhgzRyJEj9c9//lMpKSlKSUk57VN1AAAAUH/VaUmvCRMm6B//+Ify8vJqHTfGKCwsTI8++qgee+wxSVJ5eblCQkI0b948DR48WNu3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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **STEP 9 — Remove Loan_ID**\n",
        "\n",
        "**Loan_ID is just an identifier.**"
      ],
      "metadata": {
        "id": "QdjFzHbF13A4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df = df.drop('Loan_ID', axis=1)"
      ],
      "metadata": {
        "id": "esS57wy016m9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **STEP 10 — Convert Categorical Variables to Numeric**\n",
        "\n",
        "**Random Forest cannot process text.**"
      ],
      "metadata": {
        "id": "jw0TltZm2Qew"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.preprocessing import LabelEncoder\n",
        "\n",
        "le = LabelEncoder()"
      ],
      "metadata": {
        "id": "22GAbWR12ill"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Apply encoding:"
      ],
      "metadata": {
        "id": "WS4_nYii3fIj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "for col in df.columns:\n",
        "    if df[col].dtype == 'object':\n",
        "        df[col] = le.fit_transform(df[col])"
      ],
      "metadata": {
        "id": "w8mkyfe63h4e"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Check:"
      ],
      "metadata": {
        "id": "X5ixE_hT4Ehe"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "QbQkvwjo4Dnv",
        "outputId": "2443f00e-4a34-4c12-8fe7-c8ca7e0d6c00"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Gender  Married  Dependents  Education  Self_Employed  ApplicantIncome  \\\n",
              "0       1        0           0          0              0             5849   \n",
              "1       1        1           1          0              0             4583   \n",
              "2       1        1           0          0              1             3000   \n",
              "3       1        1           0          1              0             2583   \n",
              "4       1        0           0          0              0             6000   \n",
              "\n",
              "   CoapplicantIncome  LoanAmount  Loan_Amount_Term  Credit_History  \\\n",
              "0                0.0       128.0             360.0             1.0   \n",
              "1             1508.0       128.0             360.0             1.0   \n",
              "2                0.0        66.0             360.0             1.0   \n",
              "3             2358.0       120.0             360.0             1.0   \n",
              "4                0.0       141.0             360.0             1.0   \n",
              "\n",
              "   Property_Area  Loan_Status  \n",
              "0              2            1  \n",
              "1              0            0  \n",
              "2              2            1  \n",
              "3              2            1  \n",
              "4              2            1  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-db5389e1-3600-40ca-a8e0-0432bc161b37\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Gender</th>\n",
              "      <th>Married</th>\n",
              "      <th>Dependents</th>\n",
              "      <th>Education</th>\n",
              "      <th>Self_Employed</th>\n",
              "      <th>ApplicantIncome</th>\n",
              "      <th>CoapplicantIncome</th>\n",
              "      <th>LoanAmount</th>\n",
              "      <th>Loan_Amount_Term</th>\n",
              "      <th>Credit_History</th>\n",
              "      <th>Property_Area</th>\n",
              "      <th>Loan_Status</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>5849</td>\n",
              "      <td>0.0</td>\n",
              "      <td>128.0</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>4583</td>\n",
              "      <td>1508.0</td>\n",
              "      <td>128.0</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>3000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>66.0</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>2583</td>\n",
              "      <td>2358.0</td>\n",
              "      <td>120.0</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>6000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>141.0</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-db5389e1-3600-40ca-a8e0-0432bc161b37')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-db5389e1-3600-40ca-a8e0-0432bc161b37 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-db5389e1-3600-40ca-a8e0-0432bc161b37');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 614,\n  \"fields\": [\n    {\n      \"column\": \"Gender\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          0,\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Married\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Dependents\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1,\n        \"min\": 0,\n        \"max\": 3,\n        \"num_unique_values\": 4,\n        \"samples\": [\n          1,\n          3\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Education\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Self_Employed\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"ApplicantIncome\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 6109,\n        \"min\": 150,\n        \"max\": 81000,\n        \"num_unique_values\": 505,\n        \"samples\": [\n          8333,\n          4342\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"CoapplicantIncome\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 2926.2483692241917,\n        \"min\": 0.0,\n        \"max\": 41667.0,\n        \"num_unique_values\": 287,\n        \"samples\": [\n          1840.0,\n          2042.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"LoanAmount\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 84.10723338042615,\n        \"min\": 9.0,\n        \"max\": 700.0,\n        \"num_unique_values\": 203,\n        \"samples\": [\n          100.0,\n          70.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Loan_Amount_Term\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 64.42862906767301,\n        \"min\": 12.0,\n        \"max\": 480.0,\n        \"num_unique_values\": 10,\n        \"samples\": [\n          84.0,\n          120.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Credit_History\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.3523386063583013,\n        \"min\": 0.0,\n        \"max\": 1.0,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          0.0,\n          1.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Property_Area\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 2,\n        \"num_unique_values\": 3,\n        \"samples\": [\n          2,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Loan_Status\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          0,\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **STEP 11 — Separate Features and Target**"
      ],
      "metadata": {
        "id": "VJESyOA953vH"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "X = df.drop('Loan_Status', axis=1)\n",
        "\n",
        "y = df['Loan_Status']"
      ],
      "metadata": {
        "id": "zy3r9i_E57pO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X = df.drop('Loan_Status', axis=1)\n",
        "\n",
        "y = df['Loan_Status']"
      ],
      "metadata": {
        "id": "7n66zl8v6QJ0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **STEP 12 — Train Test Split**"
      ],
      "metadata": {
        "id": "Ar7N99x-6fak"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "\n",
        "X_train, X_test, y_train, y_test = train_test_split(\n",
        "    X,\n",
        "    y,\n",
        "    test_size=0.2,\n",
        "    random_state=42\n",
        ")"
      ],
      "metadata": {
        "id": "yEO8LLv06dqx"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Check:"
      ],
      "metadata": {
        "id": "_Hjhm9836wZv"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(X_train.shape)\n",
        "print(X_test.shape)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ee9ue9T46yFE",
        "outputId": "55ab3fd7-d449-41d1-caef-97bfffa84422"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(491, 11)\n",
            "(123, 11)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **STEP 13 — Train Random Forest**"
      ],
      "metadata": {
        "id": "aUJrKtiD7d0o"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.ensemble import RandomForestClassifier\n",
        "\n",
        "rf = RandomForestClassifier(\n",
        "    n_estimators=100,\n",
        "    random_state=42\n",
        ")\n",
        "\n",
        "rf.fit(X_train, y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 80
        },
        "id": "9DYvGty67hvi",
        "outputId": "9317b400-2437-473d-88b5-2464effbfb30"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "RandomForestClassifier(random_state=42)"
            ],
            "text/html": [
              "<style>#sk-container-id-1 {\n",
              "  /* Definition of color scheme common for light and dark mode */\n",
              "  --sklearn-color-text: #000;\n",
              "  --sklearn-color-text-muted: #666;\n",
              "  --sklearn-color-line: gray;\n",
              "  /* Definition of color scheme for unfitted estimators */\n",
              "  --sklearn-color-unfitted-level-0: #fff5e6;\n",
              "  --sklearn-color-unfitted-level-1: #f6e4d2;\n",
              "  --sklearn-color-unfitted-level-2: #ffe0b3;\n",
              "  --sklearn-color-unfitted-level-3: chocolate;\n",
              "  /* Definition of color scheme for fitted estimators */\n",
              "  --sklearn-color-fitted-level-0: #f0f8ff;\n",
              "  --sklearn-color-fitted-level-1: #d4ebff;\n",
              "  --sklearn-color-fitted-level-2: #b3dbfd;\n",
              "  --sklearn-color-fitted-level-3: cornflowerblue;\n",
              "\n",
              "  /* Specific color for light theme */\n",
              "  --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
              "  --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));\n",
              "  --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
              "  --sklearn-color-icon: #696969;\n",
              "\n",
              "  @media (prefers-color-scheme: dark) {\n",
              "    /* Redefinition of color scheme for dark theme */\n",
              "    --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
              "    --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));\n",
              "    --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
              "    --sklearn-color-icon: #878787;\n",
              "  }\n",
              "}\n",
              "\n",
              "#sk-container-id-1 {\n",
              "  color: var(--sklearn-color-text);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 pre {\n",
              "  padding: 0;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 input.sk-hidden--visually {\n",
              "  border: 0;\n",
              "  clip: rect(1px 1px 1px 1px);\n",
              "  clip: rect(1px, 1px, 1px, 1px);\n",
              "  height: 1px;\n",
              "  margin: -1px;\n",
              "  overflow: hidden;\n",
              "  padding: 0;\n",
              "  position: absolute;\n",
              "  width: 1px;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-dashed-wrapped {\n",
              "  border: 1px dashed var(--sklearn-color-line);\n",
              "  margin: 0 0.4em 0.5em 0.4em;\n",
              "  box-sizing: border-box;\n",
              "  padding-bottom: 0.4em;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-container {\n",
              "  /* jupyter's `normalize.less` sets `[hidden] { display: none; }`\n",
              "     but bootstrap.min.css set `[hidden] { display: none !important; }`\n",
              "     so we also need the `!important` here to be able to override the\n",
              "     default hidden behavior on the sphinx rendered scikit-learn.org.\n",
              "     See: https://github.com/scikit-learn/scikit-learn/issues/21755 */\n",
              "  display: inline-block !important;\n",
              "  position: relative;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-text-repr-fallback {\n",
              "  display: none;\n",
              "}\n",
              "\n",
              "div.sk-parallel-item,\n",
              "div.sk-serial,\n",
              "div.sk-item {\n",
              "  /* draw centered vertical line to link estimators */\n",
              "  background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));\n",
              "  background-size: 2px 100%;\n",
              "  background-repeat: no-repeat;\n",
              "  background-position: center center;\n",
              "}\n",
              "\n",
              "/* Parallel-specific style estimator block */\n",
              "\n",
              "#sk-container-id-1 div.sk-parallel-item::after {\n",
              "  content: \"\";\n",
              "  width: 100%;\n",
              "  border-bottom: 2px solid var(--sklearn-color-text-on-default-background);\n",
              "  flex-grow: 1;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-parallel {\n",
              "  display: flex;\n",
              "  align-items: stretch;\n",
              "  justify-content: center;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "  position: relative;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-parallel-item {\n",
              "  display: flex;\n",
              "  flex-direction: column;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-parallel-item:first-child::after {\n",
              "  align-self: flex-end;\n",
              "  width: 50%;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-parallel-item:last-child::after {\n",
              "  align-self: flex-start;\n",
              "  width: 50%;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-parallel-item:only-child::after {\n",
              "  width: 0;\n",
              "}\n",
              "\n",
              "/* Serial-specific style estimator block */\n",
              "\n",
              "#sk-container-id-1 div.sk-serial {\n",
              "  display: flex;\n",
              "  flex-direction: column;\n",
              "  align-items: center;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "  padding-right: 1em;\n",
              "  padding-left: 1em;\n",
              "}\n",
              "\n",
              "\n",
              "/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is\n",
              "clickable and can be expanded/collapsed.\n",
              "- Pipeline and ColumnTransformer use this feature and define the default style\n",
              "- Estimators will overwrite some part of the style using the `sk-estimator` class\n",
              "*/\n",
              "\n",
              "/* Pipeline and ColumnTransformer style (default) */\n",
              "\n",
              "#sk-container-id-1 div.sk-toggleable {\n",
              "  /* Default theme specific background. It is overwritten whether we have a\n",
              "  specific estimator or a Pipeline/ColumnTransformer */\n",
              "  background-color: var(--sklearn-color-background);\n",
              "}\n",
              "\n",
              "/* Toggleable label */\n",
              "#sk-container-id-1 label.sk-toggleable__label {\n",
              "  cursor: pointer;\n",
              "  display: flex;\n",
              "  width: 100%;\n",
              "  margin-bottom: 0;\n",
              "  padding: 0.5em;\n",
              "  box-sizing: border-box;\n",
              "  text-align: center;\n",
              "  align-items: start;\n",
              "  justify-content: space-between;\n",
              "  gap: 0.5em;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 label.sk-toggleable__label .caption {\n",
              "  font-size: 0.6rem;\n",
              "  font-weight: lighter;\n",
              "  color: var(--sklearn-color-text-muted);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 label.sk-toggleable__label-arrow:before {\n",
              "  /* Arrow on the left of the label */\n",
              "  content: \"▸\";\n",
              "  float: left;\n",
              "  margin-right: 0.25em;\n",
              "  color: var(--sklearn-color-icon);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {\n",
              "  color: var(--sklearn-color-text);\n",
              "}\n",
              "\n",
              "/* Toggleable content - dropdown */\n",
              "\n",
              "#sk-container-id-1 div.sk-toggleable__content {\n",
              "  max-height: 0;\n",
              "  max-width: 0;\n",
              "  overflow: hidden;\n",
              "  text-align: left;\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-toggleable__content.fitted {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-toggleable__content pre {\n",
              "  margin: 0.2em;\n",
              "  border-radius: 0.25em;\n",
              "  color: var(--sklearn-color-text);\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-toggleable__content.fitted pre {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {\n",
              "  /* Expand drop-down */\n",
              "  max-height: 200px;\n",
              "  max-width: 100%;\n",
              "  overflow: auto;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {\n",
              "  content: \"▾\";\n",
              "}\n",
              "\n",
              "/* Pipeline/ColumnTransformer-specific style */\n",
              "\n",
              "#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
              "  color: var(--sklearn-color-text);\n",
              "  background-color: var(--sklearn-color-unfitted-level-2);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
              "  background-color: var(--sklearn-color-fitted-level-2);\n",
              "}\n",
              "\n",
              "/* Estimator-specific style */\n",
              "\n",
              "/* Colorize estimator box */\n",
              "#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-2);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-2);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-label label.sk-toggleable__label,\n",
              "#sk-container-id-1 div.sk-label label {\n",
              "  /* The background is the default theme color */\n",
              "  color: var(--sklearn-color-text-on-default-background);\n",
              "}\n",
              "\n",
              "/* On hover, darken the color of the background */\n",
              "#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {\n",
              "  color: var(--sklearn-color-text);\n",
              "  background-color: var(--sklearn-color-unfitted-level-2);\n",
              "}\n",
              "\n",
              "/* Label box, darken color on hover, fitted */\n",
              "#sk-container-id-1 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {\n",
              "  color: var(--sklearn-color-text);\n",
              "  background-color: var(--sklearn-color-fitted-level-2);\n",
              "}\n",
              "\n",
              "/* Estimator label */\n",
              "\n",
              "#sk-container-id-1 div.sk-label label {\n",
              "  font-family: monospace;\n",
              "  font-weight: bold;\n",
              "  display: inline-block;\n",
              "  line-height: 1.2em;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-label-container {\n",
              "  text-align: center;\n",
              "}\n",
              "\n",
              "/* Estimator-specific */\n",
              "#sk-container-id-1 div.sk-estimator {\n",
              "  font-family: monospace;\n",
              "  border: 1px dotted var(--sklearn-color-border-box);\n",
              "  border-radius: 0.25em;\n",
              "  box-sizing: border-box;\n",
              "  margin-bottom: 0.5em;\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-estimator.fitted {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-0);\n",
              "}\n",
              "\n",
              "/* on hover */\n",
              "#sk-container-id-1 div.sk-estimator:hover {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-2);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-estimator.fitted:hover {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-2);\n",
              "}\n",
              "\n",
              "/* Specification for estimator info (e.g. \"i\" and \"?\") */\n",
              "\n",
              "/* Common style for \"i\" and \"?\" */\n",
              "\n",
              ".sk-estimator-doc-link,\n",
              "a:link.sk-estimator-doc-link,\n",
              "a:visited.sk-estimator-doc-link {\n",
              "  float: right;\n",
              "  font-size: smaller;\n",
              "  line-height: 1em;\n",
              "  font-family: monospace;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "  border-radius: 1em;\n",
              "  height: 1em;\n",
              "  width: 1em;\n",
              "  text-decoration: none !important;\n",
              "  margin-left: 0.5em;\n",
              "  text-align: center;\n",
              "  /* unfitted */\n",
              "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
              "  color: var(--sklearn-color-unfitted-level-1);\n",
              "}\n",
              "\n",
              ".sk-estimator-doc-link.fitted,\n",
              "a:link.sk-estimator-doc-link.fitted,\n",
              "a:visited.sk-estimator-doc-link.fitted {\n",
              "  /* fitted */\n",
              "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
              "  color: var(--sklearn-color-fitted-level-1);\n",
              "}\n",
              "\n",
              "/* On hover */\n",
              "div.sk-estimator:hover .sk-estimator-doc-link:hover,\n",
              ".sk-estimator-doc-link:hover,\n",
              "div.sk-label-container:hover .sk-estimator-doc-link:hover,\n",
              ".sk-estimator-doc-link:hover {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-3);\n",
              "  color: var(--sklearn-color-background);\n",
              "  text-decoration: none;\n",
              "}\n",
              "\n",
              "div.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,\n",
              ".sk-estimator-doc-link.fitted:hover,\n",
              "div.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,\n",
              ".sk-estimator-doc-link.fitted:hover {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-3);\n",
              "  color: var(--sklearn-color-background);\n",
              "  text-decoration: none;\n",
              "}\n",
              "\n",
              "/* Span, style for the box shown on hovering the info icon */\n",
              ".sk-estimator-doc-link span {\n",
              "  display: none;\n",
              "  z-index: 9999;\n",
              "  position: relative;\n",
              "  font-weight: normal;\n",
              "  right: .2ex;\n",
              "  padding: .5ex;\n",
              "  margin: .5ex;\n",
              "  width: min-content;\n",
              "  min-width: 20ex;\n",
              "  max-width: 50ex;\n",
              "  color: var(--sklearn-color-text);\n",
              "  box-shadow: 2pt 2pt 4pt #999;\n",
              "  /* unfitted */\n",
              "  background: var(--sklearn-color-unfitted-level-0);\n",
              "  border: .5pt solid var(--sklearn-color-unfitted-level-3);\n",
              "}\n",
              "\n",
              ".sk-estimator-doc-link.fitted span {\n",
              "  /* fitted */\n",
              "  background: var(--sklearn-color-fitted-level-0);\n",
              "  border: var(--sklearn-color-fitted-level-3);\n",
              "}\n",
              "\n",
              ".sk-estimator-doc-link:hover span {\n",
              "  display: block;\n",
              "}\n",
              "\n",
              "/* \"?\"-specific style due to the `<a>` HTML tag */\n",
              "\n",
              "#sk-container-id-1 a.estimator_doc_link {\n",
              "  float: right;\n",
              "  font-size: 1rem;\n",
              "  line-height: 1em;\n",
              "  font-family: monospace;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "  border-radius: 1rem;\n",
              "  height: 1rem;\n",
              "  width: 1rem;\n",
              "  text-decoration: none;\n",
              "  /* unfitted */\n",
              "  color: var(--sklearn-color-unfitted-level-1);\n",
              "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 a.estimator_doc_link.fitted {\n",
              "  /* fitted */\n",
              "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
              "  color: var(--sklearn-color-fitted-level-1);\n",
              "}\n",
              "\n",
              "/* On hover */\n",
              "#sk-container-id-1 a.estimator_doc_link:hover {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-3);\n",
              "  color: var(--sklearn-color-background);\n",
              "  text-decoration: none;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 a.estimator_doc_link.fitted:hover {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-3);\n",
              "}\n",
              "</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>RandomForestClassifier(random_state=42)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator fitted sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label fitted sk-toggleable__label-arrow\"><div><div>RandomForestClassifier</div></div><div><a class=\"sk-estimator-doc-link fitted\" rel=\"noreferrer\" target=\"_blank\" href=\"https://scikit-learn.org/1.6/modules/generated/sklearn.ensemble.RandomForestClassifier.html\">?<span>Documentation for RandomForestClassifier</span></a><span class=\"sk-estimator-doc-link fitted\">i<span>Fitted</span></span></div></label><div class=\"sk-toggleable__content fitted\"><pre>RandomForestClassifier(random_state=42)</pre></div> </div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **STEP 14 — Prediction**"
      ],
      "metadata": {
        "id": "KCTKq0qS77rp"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred = rf.predict(X_test)"
      ],
      "metadata": {
        "id": "Ud3OEBmm7xGk"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **STEP 15 — Accuracy**"
      ],
      "metadata": {
        "id": "WMAjmGd88MY6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import accuracy_score\n",
        "\n",
        "accuracy = accuracy_score(\n",
        "    y_test,\n",
        "    y_pred\n",
        ")\n",
        "\n",
        "print(\n",
        "    \"Accuracy:\",\n",
        "    accuracy\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gtjFM5Cw8LF_",
        "outputId": "6a76bb00-88a3-4bd0-826c-3e33c67b0f20"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy: 0.7560975609756098\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **STEP 16 — Confusion Matrix**"
      ],
      "metadata": {
        "id": "zbxFqgaB8gEl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import confusion_matrix\n",
        "\n",
        "cm = confusion_matrix(\n",
        "    y_test,\n",
        "    y_pred\n",
        ")\n",
        "\n",
        "print(cm)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ajg3Ygzd8fKW",
        "outputId": "288d9d42-87e9-480d-b669-b3da6918be5f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[18 25]\n",
            " [ 5 75]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Better Visualization**"
      ],
      "metadata": {
        "id": "7XfelGNI9BLf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "plt.figure(figsize=(6,4))\n",
        "sns.heatmap(\n",
        "    cm,\n",
        "    annot=True,\n",
        "    fmt='d',\n",
        "    cmap='Blues'\n",
        ")\n",
        "plt.title(\n",
        "    'Confusion Matrix'\n",
        ")\n",
        "plt.xlabel(\n",
        "    'Predicted'\n",
        ")\n",
        "plt.ylabel(\n",
        "    'Actual'\n",
        ")\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 410
        },
        "id": "NiJ3kcqu8_sS",
        "outputId": "57232629-31a9-437d-a4ad-ac767021f930"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 600x400 with 2 Axes>"
            ],
            "image/png": "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BQQESJJOnDhRquN//vlneXl5qWnTpi7tYWFhCgoK0s8//+zS3qhRo2LXqFu3rn777bcyVlzckCFD1KVLF911110KDQ3V0KFD9cYbb5w34M/W2bx582L7WrZsqaNHj+rUqVMu7X+9l7p160qSW/dy4403qk6dOnr99df1yiuvqGPHjsV+l2cVFRVpxowZatasmex2u+rXr6+QkBB9++23On78eKn7vOSSS9xaFPf0008rODhY27dv1+zZs9WgQYNSnwuYGaGOai8gIEARERHauXOnW+f9daHauXh7e5fYbhhGmfs4+3nvWX5+ftq0aZM++ugj/eMf/9C3336rIUOGqFevXsWOLY/y3MtZdrtd8fHxWrp0qVatWnXOUbokTZ06VUlJSbr22mv18ssva926dVq/fr2uuOKKUs9ISH/8ftyxbds2HT58WJK0Y8cOt84FzIxQx0Whb9++2rt3r9LS0i54bGRkpIqKirR7926X9uzsbOXk5DhXsleEunXruqwUP+uvswGS5OXlpeuuu07PPvusvvvuOz355JPasGGDPv744xKvfbbOjIyMYvt++OEH1a9fX7Vr1y7fDZzDrbfeqm3btunEiRMlLi48a+XKlerRo4cWLVqkoUOH6vrrr1dsbGyx30lp/4JVGqdOndLw4cPVqlUr3X333Zo+fbq2bt1aYdcHLmaEOi4KDzzwgGrXrq277rpL2dnZxfbv3btXs2bNkvTH9LGkYivUn332WUlSnz59KqyuJk2a6Pjx4/r222+dbYcOHdKqVatcjvv111+LnXv2JSx/fczurPDwcLVr105Lly51CcmdO3fqww8/dN5nZejRo4cef/xxzZ07V2FhYec8ztvbu9gswIoVK/S///3Ppe3sXz5K+guQux588EFlZmZq6dKlevbZZxUVFaWEhIRz/h4BK+HlM7goNGnSRMuXL9eQIUPUsmVLlzfKff7551qxYoWGDRsmSWrbtq0SEhK0cOFC5eTkqFu3bvryyy+1dOlSDRgw4JyPS5XF0KFD9eCDD+rvf/+7xowZo9OnT2v+/Pm6/PLLXRaKTZkyRZs2bVKfPn0UGRmpw4cPa968ebr00kvVtWvXc17/qaeeUu/evRUTE6MRI0bozJkzmjNnjgIDAzVp0qQKu4+/8vLy0iOPPHLB4/r27aspU6Zo+PDhuvrqq7Vjxw698soruuyy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OWX+5JNPKiIiQs2bN5ck/fLLLxo8eLCCgoIUHBys/v3766effnJer7CwUElJSQoKClK9evX0wAMP6K9f0fDX6XeHw6EHH3xQDRs2lN1uV9OmTbVo0SL99NNPzi8jqVu3rmw2m4YNGybpj6/JTUlJUePGjeXn56e2bdtq5cqVLv28//77uvzyy+Xn56cePXq41Amg+iHUgQrm5+en/Px8SVJqaqoyMjK0fv16vfvuuyooKFBcXJzq1KmjTz/9VJ999pn8/f11ww03OM955plntGTJEr344ovavHmzfv31V61ateq8fd5xxx169dVXNXv2bH3//fd6/vnn5e/vr4YNG+rNN9+UJGVkZOjQoUOaNWuWJCklJUUvvfSSFixYoF27dikxMVG33367Nm7cKOmPv3zEx8erX79+2r59u+666y499NBDlfVrA1ARDABllpCQYPTv398wDMMoKioy1q9fb9jtdmP8+PFGQkKCERoaajgcDufxy5YtM5o3b24UFRU52xwOh+Hn52esW7fOMAzDCA8PN6ZPn+7cX1BQYFx66aXOfgzDMLp162aMHTvWMAzDyMjIMCQZ69evL7HGjz/+2JBk/Pbbb862vLw8o1atWsbnn3/ucuyIESOMW265xTAMw0hOTjZatWrlsv/BBx8sdi0A1QefqQPl9O6778rf318FBQUqKirSrbfeqkmTJmnkyJFq3bq1y+fo33zzjfbs2aM6deq4XCMvL0979+7V8ePHdejQIZfvo69Ro4Y6dOhQbAr+rO3bt8vb21vdunUrdc179uzR6dOn1atXL5f2/Px8XXXVVZKk77//3qUOSYqJiSl1HwCqHqEOlFOPHj00f/58+fr6KiIiQjVq/N9/VrVr13Y59uTJk4qOjtYrr7xS7DohISFl6t/Pz8/tc06ePClJeu+993TJJZe47LPb7WWqA4DnEepAOdWuXVtNmzYt1bHt27fX66+/rgYNGiggIKDEY8LDw/XFF1/o2muvlST9/vvvSk9PV/v27Us8vnXr1ioqKtLGjRsVGxtbbP/ZmYLCwkJnW6tWrWS325WZmXnOEX7Lli31zjvvuLRt2bLlwjcJwGNYKAdUodtuu03169dX//799emnn2r//v365JNPNGbMGB04cECSNHbsWE2bNk2rV6/WDz/8oH/961/nfcY8KipKCQkJuvPOO7V69WrnNd944w1JUmRkpGw2m959910dOXJEJ0+eVJ06dTR+/HglJiZq6dKl2rt3r77++mvNmTNHS5culSTde++92r17tyZMmKCMjAwtX75cS5YsqexfEYByINSBKlSrVi1t2rRJjRo1Unx8vFq2bKkRI0YoLy/POXIfN26c/vGPfyghIUExMTGqU6eO/v73v5/3uvPnz9egQYP0r3/9Sy1atNA///lPnTp1SpJ0ySWXaPLkyXrooYcUGhqqUaNGSZIef/xxPfroo0pJSVHLli11ww036L333lPjxo0lSY0aNdKbb76p1atXq23btlqwYIGmTp1aib8dAOVlM861+gYAAFxUGKkDAGAShDoAACZBqAMAYBKEOgAAJkGoAwBgEoQ6AAAmQagDAGAShDoAACZBqAMAYBKEOgAAJkGoAwBgEv8PQZjTOBFIMLoAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **STEP 17 — Classification Report**"
      ],
      "metadata": {
        "id": "6vjKkRrU97XV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import classification_report\n",
        "\n",
        "print(\n",
        "    classification_report(\n",
        "        y_test,\n",
        "        y_pred\n",
        "    )\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VjI6iOcp96UP",
        "outputId": "f711ba3e-9ed7-4692-cba2-69f57f4c80aa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.78      0.42      0.55        43\n",
            "           1       0.75      0.94      0.83        80\n",
            "\n",
            "    accuracy                           0.76       123\n",
            "   macro avg       0.77      0.68      0.69       123\n",
            "weighted avg       0.76      0.76      0.73       123\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **-- STEP 18 — Feature Importance**\n",
        "\n",
        "    This is one of the coolest things about Random Forest."
      ],
      "metadata": {
        "id": "xTXcmgHo-Ue9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "importance = pd.DataFrame({\n",
        "    'Feature': X.columns,\n",
        "    'Importance': rf.feature_importances_\n",
        "})\n",
        "\n",
        "importance = importance.sort_values(\n",
        "    by='Importance',\n",
        "    ascending=False\n",
        ")\n",
        "\n",
        "importance"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 394
        },
        "id": "KlEXIXau-TA_",
        "outputId": "d710a382-704d-4c00-b9e6-3b175cedbd56"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "              Feature  Importance\n",
              "9      Credit_History    0.262914\n",
              "5     ApplicantIncome    0.202666\n",
              "7          LoanAmount    0.185022\n",
              "6   CoapplicantIncome    0.113861\n",
              "8    Loan_Amount_Term    0.051443\n",
              "10      Property_Area    0.049602\n",
              "2          Dependents    0.048141\n",
              "1             Married    0.023648\n",
              "3           Education    0.021271\n",
              "0              Gender    0.020718\n",
              "4       Self_Employed    0.020713"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-51d56ef4-a2a4-431b-a930-e7c11ca59f34\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Feature</th>\n",
              "      <th>Importance</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>Credit_History</td>\n",
              "      <td>0.262914</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>ApplicantIncome</td>\n",
              "      <td>0.202666</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>LoanAmount</td>\n",
              "      <td>0.185022</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>CoapplicantIncome</td>\n",
              "      <td>0.113861</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>Loan_Amount_Term</td>\n",
              "      <td>0.051443</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>Property_Area</td>\n",
              "      <td>0.049602</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Dependents</td>\n",
              "      <td>0.048141</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Married</td>\n",
              "      <td>0.023648</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Education</td>\n",
              "      <td>0.021271</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Gender</td>\n",
              "      <td>0.020718</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Self_Employed</td>\n",
              "      <td>0.020713</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-51d56ef4-a2a4-431b-a930-e7c11ca59f34')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-51d56ef4-a2a4-431b-a930-e7c11ca59f34 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-51d56ef4-a2a4-431b-a930-e7c11ca59f34');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "  <div id=\"id_c6562e89-7c9f-449a-866d-d6b2628b49a0\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('importance')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_c6562e89-7c9f-449a-866d-d6b2628b49a0 button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('importance');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "importance",
              "summary": "{\n  \"name\": \"importance\",\n  \"rows\": 11,\n  \"fields\": [\n    {\n      \"column\": \"Feature\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 11,\n        \"samples\": [\n          \"Property_Area\",\n          \"Credit_History\",\n          \"Gender\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Importance\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.087051875031858,\n        \"min\": 0.020712969321403922,\n        \"max\": 0.2629141259239111,\n        \"num_unique_values\": 11,\n        \"samples\": [\n          0.04960243855709676,\n          0.2629141259239111,\n          0.020717829092128517\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Visualize Feature Importance**"
      ],
      "metadata": {
        "id": "gNq8MNUt_QGl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(10,6))\n",
        "\n",
        "plt.barh(\n",
        "    importance['Feature'],\n",
        "    importance['Importance']\n",
        ")\n",
        "\n",
        "plt.title(\n",
        "    'Feature Importance'\n",
        ")\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 545
        },
        "id": "Sjd_cmkj_VDB",
        "outputId": "22c49df1-5157-4adb-fb7e-2f83ffa9cf77"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA6wAAAIQCAYAAACFROP+AAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAbS5JREFUeJzt3XlcFWX///H3QeQg4AEXFFQUUVFc0NwR9yVcc8stzXCprLRMKfU2FdxzKe02zQyhnazMvF0z7rAk98RMiVtNwgrTXEA0UeH8/vDn+XYCDdzOqK/n4zGPm3PNNdd8ZpivX95dM3NMVqvVKgAAAAAADMbJ0QUAAAAAAJAfAisAAAAAwJAIrAAAAAAAQyKwAgAAAAAMicAKAAAAADAkAisAAAAAwJAIrAAAAAAAQyKwAgAAAAAMicAKAAAAADAkAisAAAAAwJAIrAAAFEJsbKxMJlO+y/jx42/LPr/99ltFRkbqzJkzt2X8m3H1fOzatcvRpdywxYsXKzY21tFlAADy4ezoAgAAuBtNnTpVlStXtmurXbv2bdnXt99+q6ioKIWHh8vLy+u27ON+tnjxYpUuXVrh4eGOLgUA8DcEVgAAbkCnTp3UsGFDR5dxU86dOyd3d3dHl+Ew58+fl5ubm6PLAABcB7cEAwBwG6xfv14tWrSQu7u7ihcvri5dumj//v12fb7//nuFh4crICBArq6u8vHx0dChQ3Xy5Elbn8jISL3wwguSpMqVK9tuP05NTVVqaqpMJlO+t7OaTCZFRkbajWMymXTgwAE98sgjKlGihJo3b25b/95776lBgwYqVqyYSpYsqf79++vo0aM3dOzh4eHy8PBQWlqaunbtKg8PD5UvX16vv/66JGnfvn1q27at3N3dValSJX3wwQd221+9zfjrr7/Wk08+qVKlSslisWjw4ME6ffp0nv0tXrxYtWrVktlsVrly5fTMM8/kuX26devWql27tnbv3q2WLVvKzc1N//rXv+Tv76/9+/dr8+bNtnPbunVrSdKpU6cUERGhOnXqyMPDQxaLRZ06ddLevXvtxk5ISJDJZNKKFSs0Y8YMVahQQa6urmrXrp0OHTqUp97t27erc+fOKlGihNzd3RUcHKyFCxfa9fnxxx/18MMPq2TJknJ1dVXDhg21evXqwv4qAOCuxwwrAAA3ICMjQ3/88YddW+nSpSVJ7777rh577DGFhYXp5Zdf1vnz57VkyRI1b95ce/bskb+/vyRp06ZN+umnnzRkyBD5+Pho//79evPNN7V//35t27ZNJpNJvXr10v/+9z99+OGHevXVV2378Pb21okTJwpdd58+fVStWjXNnDlTVqtVkjRjxgxNmjRJffv21fDhw3XixAn9+9//VsuWLbVnz54bug05JydHnTp1UsuWLTVnzhy9//77GjlypNzd3TVx4kQNHDhQvXr10htvvKHBgwcrJCQkzy3WI0eOlJeXlyIjI5WSkqIlS5bo559/tgVE6UoQj4qKUvv27fXUU0/Z+u3cuVOJiYkqWrSobbyTJ0+qU6dO6t+/vwYNGqSyZcuqdevWGjVqlDw8PDRx4kRJUtmyZSVJP/30k1atWqU+ffqocuXK+v3337V06VK1atVKBw4cULly5ezqnT17tpycnBQREaGMjAzNmTNHAwcO1Pbt2219Nm3apK5du8rX11fPPfecfHx8lJycrDVr1ui5556TJO3fv1+hoaEqX768xo8fL3d3d61YsUI9evTQp59+qp49exb69wEAdy0rAAAosJiYGKukfBer1Wo9e/as1cvLy/r444/bbXfs2DGrp6enXfv58+fzjP/hhx9aJVm//vprW9vcuXOtkqxHjhyx63vkyBGrJGtMTEyecSRZp0yZYvs8ZcoUqyTrgAED7PqlpqZaixQpYp0xY4Zd+759+6zOzs552q91Pnbu3Glre+yxx6ySrDNnzrS1nT592lqsWDGryWSyxsXF2dp//PHHPLVeHbNBgwbWixcv2trnzJljlWT9/PPPrVar1Xr8+HGri4uL9cEHH7Tm5OTY+i1atMgqybp8+XJbW6tWraySrG+88UaeY6hVq5a1VatWedovXLhgN67VeuWcm81m69SpU21tX331lVWSNSgoyJqdnW1rX7hwoVWSdd++fVar1Wq9fPmytXLlytZKlSpZT58+bTdubm6u7ed27dpZ69SpY71w4YLd+mbNmlmrVauWp04AuJdxSzAAADfg9ddf16ZNm+wW6coM2pkzZzRgwAD98ccftqVIkSJq0qSJvvrqK9sYxYoVs/184cIF/fHHH2ratKkk6bvvvrstdY8YMcLu88qVK5Wbm6u+ffva1evj46Nq1arZ1VtYw4cPt/3s5eWl6tWry93dXX379rW1V69eXV5eXvrpp5/ybP/E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qlq1apo3b568vLz0ySef5BnPw8PD9vKgqzOlBbFv3z5beL66jBgxwq5P586d9eSTT6patWqaPHmyMjMz1ahRI/Xp00eBgYEaN26ckpOT9fvvv9u2uXTpkhYtWqSQkBA1aNBAb7/9tr799lvt2LEj3zrmzZuncePGqX///qpevbpefvll1atXTwsWLJAk9erVS5L0+eef27aJjY1VeHi4TCaT0tLSFBMTo48//lgtWrRQlSpVFBERoebNm9uC/MKFC9WxY0e9+OKLCgwM1LPPPquwsLDrnp9Zs2bJ09PTtvj5+RXovAIAAADAVXddYJWuPMP622+/afXq1erYsaMSEhJUv359xcbGau/evcrKylKpUqXswuSRI0dsz6reCtWrV1dSUpLdMnXqVLs+wcHBtp/Lli0rSapTp06etuPHj9vanJ2d1ahRI9vnGjVqyMvLS8nJyXlqyMzM1G+//abQ0FC79tDQUFt/V1dXPfroo1q+fLkk6bvvvtMPP/yg8PBwSVeCd05OjgIDA+3O1+bNm23nKzk5WU2aNLHbR0hIyHXPz4QJE5SRkWFbrndbMwAAAADk5659S5Crq6s6dOigDh06aNKkSRo+fLimTJmip59+Wr6+vnmewZR0S7+GxcXFRVWrVr1un6JFi9p+vvpsbH5tubm5t6yu/AwfPlz16tXTL7/8opiYGLVt21aVKlWSJGVlZalIkSLavXu3ihQpYredh4fHDe/TbDbLbDbfVN0AAAAA7m93bWD9u5o1a2rVqlWqX7++jh07JmdnZ/n7+zu6rEK7fPmydu3apcaNG0uSUlJSdObMGQUFBeXpa7FYVK5cOSUmJqpVq1a29sTERNv20pVZ3YYNG2rZsmX64IMPtGjRItu6Bx54QDk5OTp+/LhatGiRb01BQUHavn27Xdu2bdtu6jgBAAAA4J/cdYH15MmT6tOnj4YOHarg4GAVL15cu3bt0pw5c9S9e3e1b99eISEh6tGjh+bMmaPAwED99ttvWrt2rXr27KmGDRvekjouX76sY8eO2bWZTCbbbb43qmjRoho1apRee+01OTs7a+TIkWratKldAP2rF154QVOmTFGVKlVUr149xcTEKCkpSe+//75dv+HDh2vkyJFyd3dXz549be2BgYEaOHCgBg8erPnz5+uBBx7QiRMnFB8fr+DgYHXp0kXPPvusQkNDNW/e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KTc3N1WrVk2rV6+21dGmTRtJUokSJWQymRQeHi5J+uSTT1SnTh0VK1ZMpUqVUvv27XXu3LkbP/kAAAAAcB33fWDNT9u2bVW3bl2tXLlSktSnTx8dP35c69ev1+7du1W/fn21a9dOp06dsm1z6NAhrVixQv/5z3+0YcMG7dmzR08//bRt/fvvv6/JkydrxowZSk5O1syZMzVp0iS9/fbbdvueOHGiIiIilJSUpMDAQA0YMMAWNrdv365hw4Zp5MiRSkpKUps2bTR9+nS77b/55hsNHjxYzz33nA4cOKClS5cqNjZWM2bMsOsXFRWlvn376vvvv1fnzp01cOBAnTp1Sn5+fvr0008lSSkpKUpPT9fChQuVnp6uAQMGaOjQoUpOTlZCQoJ69eolq9Wa7znMzs5WZmam3QIAAAAAhUFgvYYaNWooNTVVW7Zs0Y4dO/Txxx+rYcOGqlatmubNmycvLy998skntv4XLlzQO++8o3r16qlly5b697//rbi4OB07dkySNGXKFM2fP1+9evVS5cqV1atXLz3//PNaunSp3X4jIiLUpUsXBQYGKioqSj///LMOHTokSVq4cKE6duyoF198UYGBgXr22WcVFhZmt31UVJTGjx+vxx57TAEBAerQoYOmTZuWZz/h4eEaMGCAqlatqpkzZyorK0s7duxQkSJFVLJkSUlSmTJl5OPjI09PT6Wnp+vy5cvq1auX/P39VadOHT399NPy8PDI9/zNmjVLnp6etsXPz+/mfiEAAAAA7jsE1muwWq0ymUzau3evsrKyVKpUKXl4eNiWI0eO6PDhw7b+FStWVPny5W2fQ0JClJubq5SUFJ07d06HDx/WsGHD7MaYPn263RiSFBwcbPvZ19dXknT8+HFJUnJyspo0aWLXPyQkxO7z3r17NXXqVLv9PP7440pPT9f58+fz3Y+7u7ssFottP/mpW7eu2rVrpzp16qhPnz5atmyZTp8+fc3+EyZMUEZGhm05evToNfsCAAAAQH6cHV2AUSUnJ6ty5crKysqSr6+vEhIS8vQp6NfJZGVlSZKWLVuWJ3AWKVLE7nPRokVtP5tMJkkq1BuLs7KyFBUVpV69euVZ5+rqmu9+ru7revspUqSINm3apG+//VZffPGF/v3vf2vixInavn27KleunKe/2WyW2WwucN0AAAAA8HcE1nz897//1b59+/T8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5qZOnTrp4MGDefaxevVq1axZU2azWVu2bFHRokV17Ngxu3pGjx6tFi1a3LLjAwAAAIC/uusD66lTp7RhwwY988wzcnd3z7P+rwEvMjJSPXv21L59+zR06FB98803Gjx4sJ577jkdOHBAS5cuVWxsrC3M5ubmqlevXnJxcdH27dv1xhtvaNy4cdesxc/PT59++qkkKSUlRenp6Vq4cOGtPeC/GDhwoCpUqKCdO3dq9+7dGj9+vIoWLapmzZppwYIFslgsSk9PV3p6uiIiIiRduf14165dWr16tbZu3Sqr1arOnTvr0qVLtnHPnz+vl19+WW+99Zb279+vhg0bKiAgQO+++66tz6VLl/T+++9r6NCht+34AAAAANzf7vpbgg8dOiSr1aoaNWr8Y99HHnlEQ4YMsX0eOnSoxo8fr8cee0ySFBAQoGnTpunFF1/UlClT9OWXX+rHH3/Uxo0bVa5cOUnSzJkz1alTp3zHL1KkiEqWLClJKlOmTKGeIV2zZo08PDzs2nJycq67TVpaml544QXbsVerVs22ztPTUyaTye525YMHD2r16tVKTExUs2bNJEnvv/++/Pz8tGrVKvXp00fSlTC6ePFi1a1b17btsGHDFBMToxdeeEGS9J///EcXLlxQ3759860tOztb2dnZts+ZmZn/eA4AAAAA4K/u+hlWq9Va4L4NGza0+7x3715NnTpVHh4etuXxxx9Xenq6zp8/r+TkZPn5+dnCqiSFhITcstr/qk2bNkpKSrJb3nrrretuM2bMGA0fPlzt27fX7Nmzdfjw4ev2T05OlrOzs5o0aWJrK1WqlKpXr67k5GRbm4uLi4KDg+22DQ8P16FDh2y3WMfGxqpv3775zmpL0qxZs+Tp6Wlb/Pz8rlsbAAAAAPzdXR9Yq1WrJpPJlO+Llf7u7+EqKytLUVFRdiFx3759OnjwoFxdXW9XydesrWrVqnZL+fLlr7tNZGSk9u/fry5duui///2vatasqc8+++ymaylWrJhMJpNdW5kyZdStWzfFxMTo999/1/r16697O/CECROUkZFhW44ePXrTdQEAAAC4v9z1twSXLFlSYWFhev311/Xss8/mCaVnzpy55q259evXV0pKiqpWrZrv+qCgIB09elTp6eny9fWVJNsM47W4uLhI+ufbeW+VwMBABQYG6vnnn9eAAQMUExOjnj17ysXFJU8NQUFBunz5srZv3267JfjkyZNKSUlRzZo1/3Ffw4cP14ABA1ShQgVVqVJFoaGh1+xrNptlNptv7uAAAAAA3Nfu+hlWSXr99deVk5Ojxo0b69NPP9XBgweVnJys11577bq38E6ePFnvvPOOoqKitH//fiUnJysuLk4vvfSSJKl9+/YKDAzUY489pr179+qbb77RxIkTr1tLpUqVZDKZtGbNGp04cUJZWVm39Fiv+vPPPzVy5EglJCTo559/VmJionbu3KmgoCBJkr+/v7KyshQfH68//vhD58+fV7Vq1dS9e3c9/vjj2rJli/bu3atBgwapfPny6t69+z/uMywsTBaLRdOnT7d7FhgAAAAAbod7IrAGBATou+++U5s2bTR27FjVrl1bHTp0UHx8vJYsWXLN7cLCwrRmzRp98cUXatSokZo2bapXX31VlSpVkiQ5OTnps88+059//qnGjRtr+PDhtjcIX0v58uUVFRWl8ePHq2zZsho5cuQtPdarihQpopMnT2rw4MEKDAxU37591alTJ0VFRUmSmjVrphEjRqhfv37y9vbWnDlzJEkxMTFq0KCBunbtqpCQEFmtVq1bt65A30nr5OSk8PBw5eTkaPDgwbfluAAAAADgKpO1MG8twn1v2LBhOnHihFavXl2o7TIzM6+8fGn0CjmZ3W5TdQAAAAD+LnV2F0eXYOdqNsjIyJDFYrlu37v+GVbcGRkZGdq3b58++OCDQodVAAAAALgRBNbbLC0t7bovNDpw4IAqVqx4Byu6Md27d9eOHTs0YsQIdejQwdHlAAAAALgPEFhvs3LlyikpKem66+8GCQkJji4BAAAAwH2GwHqbOTs7X/NrcwAAAAAA13ZPvCUYAAAAAHDvIbACAAAAAAyJwAoAAAAAMCQCKwAAAADAkAisAAAAAABD4i3BuKN+iAqTxWJxdBkAAAAA7gLMsAIAAAAADInACgAAAAAwJAIrAAAAAMCQCKwAAAAAAEMisAIAAAAADInACgAAAAAwJAIrAAAAAMCQCKwAAAAAAEMisAIAAAAADInACgAAAAAwJAIrAAAAAMCQCKwAAAAAAEMisAIAAAAADInACgAAAAAwJAIrAAAAAMCQCKwAAAAAAEMisAIAAAAADInACgAAAAAwJAIrAAAAAMCQnB1dAO4PVqtVkpSZmengSgAAAAA40tVMcDUjXA+BFXfEyZMnJUl+fn4OrgQAAACAEZw9e1aenp7X7UNgxR1RsmRJSVJaWto/XpSAdOW/vPn5+eno0aOyWCyOLgcGx/WCwuB6QWFxzaAwuF7+mdVq1dmzZ1WuXLl/7EtgxR3h5HTlcWlPT0/+DxeFYrFYuGZQYFwvKAyuFxQW1wwKg+vl+go6icVLlwAAAAAAhkRgBQAAAAAYEoEVd4TZbNaUKVNkNpsdXQruElwzKAyuFxQG1wsKi2sGhcH1cmuZrAV5lzAAAAAAAHcYM6wAAAAAAEMisAIAAAAADInACgAAAAAwJAIrAAAAAMCQCKy4Ya+//rr8/f3l6uqqJk2aaMeOHdft//HHH6tGjRpydXVVnTp1tG7dOrv1VqtVkydPlq+vr4oVK6b27dvr4MGDt/MQcAfd6uslPDxcJpPJbunYsePtPATcQYW5Xvbv36/evXvL399fJpNJCxYsuOkxcfe51ddMZGRknn9jatSocRuPAHdSYa6XZcuWqUWLFipRooRKlCih9u3b5+nP3zD3vlt9zfB3TMERWHFDPvroI40ZM0ZTpkzRd999p7p16yosLEzHjx/Pt/+3336rAQMGaNiwYdqzZ4969OihHj166IcffrD1mTNnjl577TW98cYb2r59u9zd3RUWFqYLFy7cqcPCbXI7rhdJ6tixo9LT023Lhx9+eCcOB7dZYa+X8+fPKyAgQLNnz5aPj88tGRN3l9txzUhSrVq17P6N2bJly+06BNxBhb1eEhISNGDAAH311VfaunWr/Pz89OCDD+rXX3+19eFvmHvb7bhmJP6OKTArcAMaN25sfeaZZ2yfc3JyrOXKlbPOmjUr3/59+/a1dunSxa6tSZMm1ieffNJqtVqtubm5Vh8fH+vcuXNt68+cOWM1m83WDz/88DYcAe6kW329WK1W62OPPWbt3r37bakXjlXY6+WvKlWqZH311Vdv6ZgwvttxzUyZMsVat27dW1gljOJm/z24fPmytXjx4ta3337barXyN8z94FZfM1Yrf8cUBjOsKLSLFy9q9+7dat++va3NyclJ7du319atW/PdZuvWrXb9JSksLMzW/8iRIzp27JhdH09PTzVp0uSaY+LucDuul6sSEhJUpkwZVa9eXU899ZROnjx56w8Ad9SNXC+OGBPGcTt/vwcPHlS5cuUUEBCggQMHKi0t7WbLhYPdiuvl/PnzunTpkkqWLCmJv2HudbfjmrmKv2MKhsCKQvvjjz+Uk5OjsmXL2rWXLVtWx44dy3ebY8eOXbf/1f8tzJi4O9yO60W6chvNO++8o/j4eL388svavHmzOnXqpJycnFt/ELhjbuR6ccSYMI7b9ftt0qSJYmNjtWHDBi1ZskRHjhxRixYtdPbs2ZstGQ50K66XcePGqVy5crYAw98w97bbcc1I/B1TGM6OLgAAbkT//v1tP9epU0fBwcGqUqWKEhIS1K5dOwdWBuBe0KlTJ9vPwcHBatKkiSpVqqQVK1Zo2LBhDqwMjjR79mzFxcUpISFBrq6uji4Hd4FrXTP8HVNwzLCi0EqXLq0iRYro999/t2v//fffr/nyCh8fn+v2v/q/hRkTd4fbcb3kJyAgQKVLl9ahQ4duvmg4zI1cL44YE8Zxp36/Xl5eCgwM5N+Yu9zNXC/z5s3T7Nmz9cUXXyg4ONjWzt8w97bbcc3kh79jro3AikJzcXFRgwYNFB8fb2vLzc1VfHy8QkJC8t0mJCTErr8kbdq0yda/cuXK8vHxseuTmZmp7du3X3NM3B1ux/WSn19++UUnT56Ur6/vrSkcDnEj14sjxoRx3Knfb1ZWlg4fPsy/MXe5G71e5syZo2nTpmnDhg1q2LCh3Tr+hrm33Y5rJj/8HXMdjn7rE+5OcXFxVrPZbI2NjbUeOHDA+sQTT1i9vLysx44ds1qtVuujjz5qHT9+vK1/YmKi1dnZ2Tpv3jxrcnKydcqUKdaiRYta9+3bZ+sze/Zsq5eXl/Xzzz+3fv/999bu3btbK1eubP3zzz/v+PHh1rrV18vZs2etERER1q1bt1qPHDli/fLLL63169e3VqtWzXrhwgWHHCNuncJeL9nZ2dY9e/ZY9+zZY/X19bVGRERY9+zZYz148GCBx8Td7XZcM2PHjrUmJCRYjxw5Yk1MTLS2b9/eWrp0aevx48fv+PHh1irs9TJ79myri4uL9ZNPPrGmp6fblrNnz9r14W+Ye9etvmb4O6ZwCKy4Yf/+97+tFStWtLq4uFgbN25s3bZtm21dq1atrI899phd/xUrVlgDAwOtLi4u1lq1alnXrl1rtz43N9c6adIka9myZa1ms9narl07a0pKyp04FNwBt/J6OX/+vPXBBx+0ent7W4sWLWqtVKmS9fHHHyd83EMKc70cOXLEKinP0qpVqwKPibvfrb5m+vXrZ/X19bW6uLhYy5cvb+3Xr5/10KFDd/CIcDsV5nqpVKlSvtfLlClTbH34G+bedyuvGf6OKRyT1Wq13tk5XQAAAAAA/hnPsAIAAAAADInACgAAAAAwJAIrAAAAAMCQCKwAAAAAAEMisAIAAAAADInACgAAAAAwJAIrAAAAAMCQCKwAAAAAAEMisAIAAAAADInACgAAAAAwJAIrAAAAAMCQCKwAAAAAAEP6f56ZAiuDO1HWAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ]
    }
  ]
}
