{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMjmRdQJLELuv98tkwimVj5",
      "include_colab_link": true
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
        "<a href=\"https://colab.research.google.com/github/TrinityAmyah/TrinityAmyah/blob/main/fqhc_data_cleaning.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 49,
      "metadata": {
        "id": "3nPJrmSp8X46"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import numpy as np"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iHW2tBS2iCe2",
        "outputId": "7325e597-3b40-4a3d-82a5-fb6e51328331"
      },
      "execution_count": 50,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_csv('/content/drive/MyDrive/PortfolioProject/hospital_appointment_no_show_5000.csv')"
      ],
      "metadata": {
        "id": "c6_JIUx0ifiC"
      },
      "execution_count": 51,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_csv('/kaggle/hospital_appointment_no_show_5000.csv')\n",
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 290
        },
        "id": "1XRN16xv_wXn",
        "outputId": "fd954b43-f7d0-4527-8f79-3f5f83a34931"
      },
      "execution_count": 52,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   patient_id   age  gender city_type  distance_km  travel_time_min  \\\n",
              "0           1  47.0  Female  Suburban         16.5             77.3   \n",
              "1           2  37.0    Male  Suburban          6.7             26.9   \n",
              "2           3  49.0  Female     Rural          8.2             46.1   \n",
              "3           4  62.0  Female     Urban          2.6             15.2   \n",
              "4           5  36.0  Female  Suburban          4.1             13.8   \n",
              "\n",
              "  appointment_day appointment_time_slot        department  waiting_days  ...  \\\n",
              "0             Sat               Evening        Pediatrics             8  ...   \n",
              "1             Tue               Morning        Cardiology             8  ...   \n",
              "2             Sat               Evening  General Medicine             3  ...   \n",
              "3             Thu               Evening  General Medicine            12  ...   \n",
              "4             Fri               Morning       Dermatology             8  ...   \n",
              "\n",
              "   chronic_disease  sms_reminder  email_reminder  num_reminders  \\\n",
              "0                0             1             0.0              1   \n",
              "1                1             1             0.0              2   \n",
              "2                0             1             0.0              1   \n",
              "3                1             0             1.0              1   \n",
              "4                0             1             0.0              1   \n",
              "\n",
              "   employment_status  education_level  insurance_status  rainy_day  \\\n",
              "0                NaN           Higher         Uninsured          1   \n",
              "1           Employed        Secondary           Insured          0   \n",
              "2         Unemployed        Secondary           Insured          0   \n",
              "3                NaN        Secondary           Insured          0   \n",
              "4                NaN        Secondary           Insured          0   \n",
              "\n",
              "  public_holiday no_show  \n",
              "0              0       1  \n",
              "1              1       0  \n",
              "2              0       1  \n",
              "3              0       0  \n",
              "4              0       1  \n",
              "\n",
              "[5 rows x 24 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-681566a3-7a52-405f-ac73-e5badeb2ab13\" class=\"colab-df-container\">\n",
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
              "      <th>patient_id</th>\n",
              "      <th>age</th>\n",
              "      <th>gender</th>\n",
              "      <th>city_type</th>\n",
              "      <th>distance_km</th>\n",
              "      <th>travel_time_min</th>\n",
              "      <th>appointment_day</th>\n",
              "      <th>appointment_time_slot</th>\n",
              "      <th>department</th>\n",
              "      <th>waiting_days</th>\n",
              "      <th>...</th>\n",
              "      <th>chronic_disease</th>\n",
              "      <th>sms_reminder</th>\n",
              "      <th>email_reminder</th>\n",
              "      <th>num_reminders</th>\n",
              "      <th>employment_status</th>\n",
              "      <th>education_level</th>\n",
              "      <th>insurance_status</th>\n",
              "      <th>rainy_day</th>\n",
              "      <th>public_holiday</th>\n",
              "      <th>no_show</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>47.0</td>\n",
              "      <td>Female</td>\n",
              "      <td>Suburban</td>\n",
              "      <td>16.5</td>\n",
              "      <td>77.3</td>\n",
              "      <td>Sat</td>\n",
              "      <td>Evening</td>\n",
              "      <td>Pediatrics</td>\n",
              "      <td>8</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Higher</td>\n",
              "      <td>Uninsured</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>37.0</td>\n",
              "      <td>Male</td>\n",
              "      <td>Suburban</td>\n",
              "      <td>6.7</td>\n",
              "      <td>26.9</td>\n",
              "      <td>Tue</td>\n",
              "      <td>Morning</td>\n",
              "      <td>Cardiology</td>\n",
              "      <td>8</td>\n",
              "      <td>...</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "      <td>2</td>\n",
              "      <td>Employed</td>\n",
              "      <td>Secondary</td>\n",
              "      <td>Insured</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>49.0</td>\n",
              "      <td>Female</td>\n",
              "      <td>Rural</td>\n",
              "      <td>8.2</td>\n",
              "      <td>46.1</td>\n",
              "      <td>Sat</td>\n",
              "      <td>Evening</td>\n",
              "      <td>General Medicine</td>\n",
              "      <td>3</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1</td>\n",
              "      <td>Unemployed</td>\n",
              "      <td>Secondary</td>\n",
              "      <td>Insured</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>62.0</td>\n",
              "      <td>Female</td>\n",
              "      <td>Urban</td>\n",
              "      <td>2.6</td>\n",
              "      <td>15.2</td>\n",
              "      <td>Thu</td>\n",
              "      <td>Evening</td>\n",
              "      <td>General Medicine</td>\n",
              "      <td>12</td>\n",
              "      <td>...</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Secondary</td>\n",
              "      <td>Insured</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>36.0</td>\n",
              "      <td>Female</td>\n",
              "      <td>Suburban</td>\n",
              "      <td>4.1</td>\n",
              "      <td>13.8</td>\n",
              "      <td>Fri</td>\n",
              "      <td>Morning</td>\n",
              "      <td>Dermatology</td>\n",
              "      <td>8</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Secondary</td>\n",
              "      <td>Insured</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>5 rows × 24 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-681566a3-7a52-405f-ac73-e5badeb2ab13')\"\n",
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
              "        document.querySelector('#df-681566a3-7a52-405f-ac73-e5badeb2ab13 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-681566a3-7a52-405f-ac73-e5badeb2ab13');\n",
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
              "variable_name": "df"
            }
          },
          "metadata": {},
          "execution_count": 52
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
        "id": "CKxxiaP5DTLu",
        "outputId": "af4514ee-30a1-4689-8ec4-08f9c7949caa"
      },
      "execution_count": 53,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(5000, 24)"
            ]
          },
          "metadata": {},
          "execution_count": 53
        }
      ]
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
        "id": "A6ZMhkk8DfFW",
        "outputId": "a7219d77-5da4-4ecd-fdc5-e50a632450bc"
      },
      "execution_count": 54,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 5000 entries, 0 to 4999\n",
            "Data columns (total 24 columns):\n",
            " #   Column                 Non-Null Count  Dtype  \n",
            "---  ------                 --------------  -----  \n",
            " 0   patient_id             5000 non-null   int64  \n",
            " 1   age                    4610 non-null   float64\n",
            " 2   gender                 5000 non-null   object \n",
            " 3   city_type              5000 non-null   object \n",
            " 4   distance_km            4612 non-null   float64\n",
            " 5   travel_time_min        4584 non-null   float64\n",
            " 6   appointment_day        5000 non-null   object \n",
            " 7   appointment_time_slot  5000 non-null   object \n",
            " 8   department             5000 non-null   object \n",
            " 9   waiting_days           5000 non-null   int64  \n",
            " 10  previous_appointments  5000 non-null   int64  \n",
            " 11  previous_no_shows      5000 non-null   int64  \n",
            " 12  diabetes               5000 non-null   int64  \n",
            " 13  hypertension           5000 non-null   int64  \n",
            " 14  chronic_disease        5000 non-null   int64  \n",
            " 15  sms_reminder           5000 non-null   int64  \n",
            " 16  email_reminder         4560 non-null   float64\n",
            " 17  num_reminders          5000 non-null   int64  \n",
            " 18  employment_status      4612 non-null   object \n",
            " 19  education_level        4609 non-null   object \n",
            " 20  insurance_status       5000 non-null   object \n",
            " 21  rainy_day              5000 non-null   int64  \n",
            " 22  public_holiday         5000 non-null   int64  \n",
            " 23  no_show                5000 non-null   int64  \n",
            "dtypes: float64(4), int64(12), object(8)\n",
            "memory usage: 937.6+ KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "duplicate_count = df.duplicated(subset=['patient_id']).sum()\n",
        "print(f'Number of duplicate Patient IDs: {duplicate_count}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MjszteW0Hlsz",
        "outputId": "48393d8b-98d7-40a7-ab91-dd14199dd03c"
      },
      "execution_count": 55,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Number of duplicate Patient IDs: 0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "Fx23snT4vR5P"
      }
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4abdff9f"
      },
      "source": [
        "yes_no_binary_columns = ['chronic_disease', 'sms_reminder', 'email_reminder', 'public_holiday', 'no_show']\n",
        "for col in yes_no_binary_columns:\n",
        "  if col in df.columns:\n",
        "    df[col] = df[col].astype('Int64')"
      ],
      "execution_count": 56,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.to_csv('/content/drive/MyDrive/PortfolioProject/hospital_appointment_no_show_5000_cleaned.csv', index=False)"
      ],
      "metadata": {
        "id": "lDHPVnEUBKZG"
      },
      "execution_count": 59,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print('All clean! Ready for SQL.')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hhbCJDOhwpsZ",
        "outputId": "dee17f16-3770-4e82-e2c7-4c1635f9b632"
      },
      "execution_count": 58,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "All clean! Ready for SQL.\n"
          ]
        }
      ]
    }
  ]
}