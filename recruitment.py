{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "recruitment",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPBUlgMgeuh/Ue1w26YtWai",
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
        "<a href=\"https://colab.research.google.com/github/surbhi139/recruitment/blob/main/recruitment.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**APPLICATION OF MACHINE LEARNING IN RECRUITMENT**"
      ],
      "metadata": {
        "id": "ueUBJqcRbq6B"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "IMPORTING THE LIBRARIES"
      ],
      "metadata": {
        "id": "scK85OiHb2HX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "import sklearn "
      ],
      "metadata": {
        "id": "Faluqt3SV8pq"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "IMPORTING THE DATASET"
      ],
      "metadata": {
        "id": "HsowFE1kb54H"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dataset=pd.read_excel(\"Placement_Data_Full_Class.xlsx\")\n",
        "dataset"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 522
        },
        "id": "joHBIsDAV9t-",
        "outputId": "ad06b3e2-511e-4099-b023-6bbf00f4c125"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "\n",
              "  <div id=\"df-7084336b-ebf5-403c-8fa5-ce4d9332be77\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>sl_no</th>\n",
              "      <th>gender</th>\n",
              "      <th>ssc_p</th>\n",
              "      <th>ssc_b</th>\n",
              "      <th>hsc_p</th>\n",
              "      <th>hsc_b</th>\n",
              "      <th>hsc_s</th>\n",
              "      <th>degree_p</th>\n",
              "      <th>degree_t</th>\n",
              "      <th>workex</th>\n",
              "      <th>etest_p</th>\n",
              "      <th>specialisation</th>\n",
              "      <th>mba_p</th>\n",
              "      <th>status</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>M</td>\n",
              "      <td>67.00</td>\n",
              "      <td>Others</td>\n",
              "      <td>91.00</td>\n",
              "      <td>Others</td>\n",
              "      <td>Commerce</td>\n",
              "      <td>58.00</td>\n",
              "      <td>Sci&amp;Tech</td>\n",
              "      <td>No</td>\n",
              "      <td>55.0</td>\n",
              "      <td>Mkt&amp;HR</td>\n",
              "      <td>58.80</td>\n",
              "      <td>Placed</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>M</td>\n",
              "      <td>79.33</td>\n",
              "      <td>Central</td>\n",
              "      <td>78.33</td>\n",
              "      <td>Others</td>\n",
              "      <td>Science</td>\n",
              "      <td>77.48</td>\n",
              "      <td>Sci&amp;Tech</td>\n",
              "      <td>Yes</td>\n",
              "      <td>86.5</td>\n",
              "      <td>Mkt&amp;Fin</td>\n",
              "      <td>66.28</td>\n",
              "      <td>Placed</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>M</td>\n",
              "      <td>65.00</td>\n",
              "      <td>Central</td>\n",
              "      <td>68.00</td>\n",
              "      <td>Central</td>\n",
              "      <td>Arts</td>\n",
              "      <td>64.00</td>\n",
              "      <td>Comm&amp;Mgmt</td>\n",
              "      <td>No</td>\n",
              "      <td>75.0</td>\n",
              "      <td>Mkt&amp;Fin</td>\n",
              "      <td>57.80</td>\n",
              "      <td>Placed</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>M</td>\n",
              "      <td>56.00</td>\n",
              "      <td>Central</td>\n",
              "      <td>52.00</td>\n",
              "      <td>Central</td>\n",
              "      <td>Science</td>\n",
              "      <td>52.00</td>\n",
              "      <td>Sci&amp;Tech</td>\n",
              "      <td>No</td>\n",
              "      <td>66.0</td>\n",
              "      <td>Mkt&amp;HR</td>\n",
              "      <td>59.43</td>\n",
              "      <td>Not Placed</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>M</td>\n",
              "      <td>85.80</td>\n",
              "      <td>Central</td>\n",
              "      <td>73.60</td>\n",
              "      <td>Central</td>\n",
              "      <td>Commerce</td>\n",
              "      <td>73.30</td>\n",
              "      <td>Comm&amp;Mgmt</td>\n",
              "      <td>No</td>\n",
              "      <td>96.8</td>\n",
              "      <td>Mkt&amp;Fin</td>\n",
              "      <td>55.50</td>\n",
              "      <td>Placed</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>210</th>\n",
              "      <td>211</td>\n",
              "      <td>M</td>\n",
              "      <td>80.60</td>\n",
              "      <td>Others</td>\n",
              "      <td>82.00</td>\n",
              "      <td>Others</td>\n",
              "      <td>Commerce</td>\n",
              "      <td>77.60</td>\n",
              "      <td>Comm&amp;Mgmt</td>\n",
              "      <td>No</td>\n",
              "      <td>91.0</td>\n",
              "      <td>Mkt&amp;Fin</td>\n",
              "      <td>74.49</td>\n",
              "      <td>Placed</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>211</th>\n",
              "      <td>212</td>\n",
              "      <td>M</td>\n",
              "      <td>58.00</td>\n",
              "      <td>Others</td>\n",
              "      <td>60.00</td>\n",
              "      <td>Others</td>\n",
              "      <td>Science</td>\n",
              "      <td>72.00</td>\n",
              "      <td>Sci&amp;Tech</td>\n",
              "      <td>No</td>\n",
              "      <td>74.0</td>\n",
              "      <td>Mkt&amp;Fin</td>\n",
              "      <td>53.62</td>\n",
              "      <td>Placed</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>212</th>\n",
              "      <td>213</td>\n",
              "      <td>M</td>\n",
              "      <td>67.00</td>\n",
              "      <td>Others</td>\n",
              "      <td>67.00</td>\n",
              "      <td>Others</td>\n",
              "      <td>Commerce</td>\n",
              "      <td>73.00</td>\n",
              "      <td>Comm&amp;Mgmt</td>\n",
              "      <td>Yes</td>\n",
              "      <td>59.0</td>\n",
              "      <td>Mkt&amp;Fin</td>\n",
              "      <td>69.72</td>\n",
              "      <td>Placed</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>213</th>\n",
              "      <td>214</td>\n",
              "      <td>F</td>\n",
              "      <td>74.00</td>\n",
              "      <td>Others</td>\n",
              "      <td>66.00</td>\n",
              "      <td>Others</td>\n",
              "      <td>Commerce</td>\n",
              "      <td>58.00</td>\n",
              "      <td>Comm&amp;Mgmt</td>\n",
              "      <td>No</td>\n",
              "      <td>70.0</td>\n",
              "      <td>Mkt&amp;HR</td>\n",
              "      <td>60.23</td>\n",
              "      <td>Placed</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>214</th>\n",
              "      <td>215</td>\n",
              "      <td>M</td>\n",
              "      <td>62.00</td>\n",
              "      <td>Central</td>\n",
              "      <td>58.00</td>\n",
              "      <td>Others</td>\n",
              "      <td>Science</td>\n",
              "      <td>53.00</td>\n",
              "      <td>Comm&amp;Mgmt</td>\n",
              "      <td>No</td>\n",
              "      <td>89.0</td>\n",
              "      <td>Mkt&amp;HR</td>\n",
              "      <td>60.22</td>\n",
              "      <td>Not Placed</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>215 rows × 14 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-7084336b-ebf5-403c-8fa5-ce4d9332be77')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
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
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-7084336b-ebf5-403c-8fa5-ce4d9332be77 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-7084336b-ebf5-403c-8fa5-ce4d9332be77');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ],
            "text/plain": [
              "     sl_no gender  ssc_p    ssc_b  ...  etest_p specialisation  mba_p      status\n",
              "0        1      M  67.00   Others  ...     55.0         Mkt&HR  58.80      Placed\n",
              "1        2      M  79.33  Central  ...     86.5        Mkt&Fin  66.28      Placed\n",
              "2        3      M  65.00  Central  ...     75.0        Mkt&Fin  57.80      Placed\n",
              "3        4      M  56.00  Central  ...     66.0         Mkt&HR  59.43  Not Placed\n",
              "4        5      M  85.80  Central  ...     96.8        Mkt&Fin  55.50      Placed\n",
              "..     ...    ...    ...      ...  ...      ...            ...    ...         ...\n",
              "210    211      M  80.60   Others  ...     91.0        Mkt&Fin  74.49      Placed\n",
              "211    212      M  58.00   Others  ...     74.0        Mkt&Fin  53.62      Placed\n",
              "212    213      M  67.00   Others  ...     59.0        Mkt&Fin  69.72      Placed\n",
              "213    214      F  74.00   Others  ...     70.0         Mkt&HR  60.23      Placed\n",
              "214    215      M  62.00  Central  ...     89.0         Mkt&HR  60.22  Not Placed\n",
              "\n",
              "[215 rows x 14 columns]"
            ]
          },
          "metadata": {},
          "execution_count": 58
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dataset.describe()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "id": "zBbMfpkKdL_Q",
        "outputId": "700b516a-e224-4c98-b637-c5ba34dc3661"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "\n",
              "  <div id=\"df-3343f367-e808-4a83-ad13-5c74e685338e\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>sl_no</th>\n",
              "      <th>ssc_p</th>\n",
              "      <th>hsc_p</th>\n",
              "      <th>degree_p</th>\n",
              "      <th>etest_p</th>\n",
              "      <th>mba_p</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>215.000000</td>\n",
              "      <td>215.000000</td>\n",
              "      <td>215.000000</td>\n",
              "      <td>215.000000</td>\n",
              "      <td>215.000000</td>\n",
              "      <td>215.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>108.000000</td>\n",
              "      <td>67.303395</td>\n",
              "      <td>66.333163</td>\n",
              "      <td>66.370186</td>\n",
              "      <td>72.100558</td>\n",
              "      <td>62.278186</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>62.209324</td>\n",
              "      <td>10.827205</td>\n",
              "      <td>10.897509</td>\n",
              "      <td>7.358743</td>\n",
              "      <td>13.275956</td>\n",
              "      <td>5.833385</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>1.000000</td>\n",
              "      <td>40.890000</td>\n",
              "      <td>37.000000</td>\n",
              "      <td>50.000000</td>\n",
              "      <td>50.000000</td>\n",
              "      <td>51.210000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>54.500000</td>\n",
              "      <td>60.600000</td>\n",
              "      <td>60.900000</td>\n",
              "      <td>61.000000</td>\n",
              "      <td>60.000000</td>\n",
              "      <td>57.945000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>108.000000</td>\n",
              "      <td>67.000000</td>\n",
              "      <td>65.000000</td>\n",
              "      <td>66.000000</td>\n",
              "      <td>71.000000</td>\n",
              "      <td>62.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>161.500000</td>\n",
              "      <td>75.700000</td>\n",
              "      <td>73.000000</td>\n",
              "      <td>72.000000</td>\n",
              "      <td>83.500000</td>\n",
              "      <td>66.255000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>215.000000</td>\n",
              "      <td>89.400000</td>\n",
              "      <td>97.700000</td>\n",
              "      <td>91.000000</td>\n",
              "      <td>98.000000</td>\n",
              "      <td>77.890000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-3343f367-e808-4a83-ad13-5c74e685338e')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
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
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-3343f367-e808-4a83-ad13-5c74e685338e button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-3343f367-e808-4a83-ad13-5c74e685338e');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ],
            "text/plain": [
              "            sl_no       ssc_p       hsc_p    degree_p     etest_p       mba_p\n",
              "count  215.000000  215.000000  215.000000  215.000000  215.000000  215.000000\n",
              "mean   108.000000   67.303395   66.333163   66.370186   72.100558   62.278186\n",
              "std     62.209324   10.827205   10.897509    7.358743   13.275956    5.833385\n",
              "min      1.000000   40.890000   37.000000   50.000000   50.000000   51.210000\n",
              "25%     54.500000   60.600000   60.900000   61.000000   60.000000   57.945000\n",
              "50%    108.000000   67.000000   65.000000   66.000000   71.000000   62.000000\n",
              "75%    161.500000   75.700000   73.000000   72.000000   83.500000   66.255000\n",
              "max    215.000000   89.400000   97.700000   91.000000   98.000000   77.890000"
            ]
          },
          "metadata": {},
          "execution_count": 59
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "EXPLORATORY DATA ANALYSIS"
      ],
      "metadata": {
        "id": "6ivnFjEkc4pF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(14,25))\n",
        "for i,j in zip(num,range(1,len(num)+1)):\n",
        "    plt.subplot(5,2,j)\n",
        "    sns.boxplot(dataset[i],color='lightblue')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "4S5GK6IGklhw",
        "outputId": "c1a431df-18a9-4612-ee1e-5d4e9a2e1c19"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n",
            "/usr/local/lib/python3.7/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n",
            "/usr/local/lib/python3.7/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n",
            "/usr/local/lib/python3.7/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n",
            "/usr/local/lib/python3.7/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n",
            "/usr/local/lib/python3.7/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n",
            "/usr/local/lib/python3.7/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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C+IEAABoQZwAAAAtiBMAAKAFcQIAALQgTgAAgBbECQAA0MJc4+TOO+/M1VdfnU984hM7uux2r3/VVVflFa94xZYuD6yf7RxTdnM789ouAOzEItepucbJ9ddfn1tuuSVvectbdnTZ7V7/Qx/6UG699dYtXR5YP9s5puzmdua1XQDYiUWuU3OLkzvvvDNHjx7NGCNHjx693xI722V3cv2Tjhw54jeUwGfYzjFlN7fzkY98ZC7bBYCdmNf6eC775rWh66+/PmOMJMkYI295y1tyxRVXbPmyJ09v9fr33nvv33x97733nvPyx44dyz333JNrrrlm5zvHZ7W5uZn7ar0/4nT3J+7I5p3HPdYWYHNzM+eff/5nnLedY9IDceZ2Xvva185lu+yMNWHvWAf2hrWlr7OtPctgXuvjuWzpKFFVL6yqI1V15Pbbb9/Rhm688ca/CYZ77703N95447Yuu93rn5zU088DOGk7x5Td3M5tt902l+2um91YpwCY3/p4Llt65WSMcXWSq5Pk8ssvH5/l4md16aWX5siRI7n33ntz3nnn5dJLL932Zbdz/be97W2fESjnuvzGxkaS5Morr9zJbrFF11xzTY6duHvRw1ioCy58WDb2X+CxtgBn+43ido5JD8SZ29nY2MixY8f2fLvrZjfWqcSasJesA3vD2tLXsr6aNa/18Vzm9vrqs571rFRVkqSq8uxnP3tbl93u9c8777y/+fq8886738sD62c7x5Td3M7zn//8uWwXAHZiXuvjucwtTh760IfmsssuS1Xlsssuy4UXXrity+7k+iddfvnl93t5YP1s55iym9t51KMeNZftAsBOzGt9PJe5fSA+mZXYRz/60S0V2Nkuu93rf+QjH8kYw28mgbPazjFlN7czr+0CwE4scp2aa5w89KEPzQtf+MIdX3a71/+hH/qhbY8RWB/bOabs5nbmtV0A2IlFrlP+ph8AANCCOAEAAFoQJwAAQAviBAAAaEGcAAAALYgTAACgBXECAAC0IE4AAIAWxAkAANCCOAEAAFoQJwAAQAviBAAAaEGcAAAALYgTAACgBXECAAC0IE4AAIAWxAkAANCCOAEAAFoQJwAAQAviBAAAaEGcAAAALYgTAACgBXECAAC0IE4AAIAWxAkAANCCOAEAAFoQJwAAQAviBAAAaEGcAAAALYgTAACgBXECAAC0IE4A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\n",
            "text/plain": [
              "<Figure size 1008x1800 with 7 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(10,7))\n",
        "sns.heatmap(dataset.corr(),annot=True, cmap=\"Purples\")\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 433
        },
        "id": "uLTTc2ytd8E4",
        "outputId": "464d8178-16e5-4de4-a727-d90835ba2637"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 720x504 with 2 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.countplot(dataset['degree_t'])\n",
        "dataset['degree_t'].value_counts(normalize=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 404
        },
        "id": "u1aAmq64epic",
        "outputId": "abe079d0-42f7-44ae-ae89-b4039dcd30f1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Comm&Mgmt    0.674419\n",
              "Sci&Tech     0.274419\n",
              "Others       0.051163\n",
              "Name: degree_t, dtype: float64"
            ]
          },
          "metadata": {},
          "execution_count": 62
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dataset.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gko_UqrxdTNd",
        "outputId": "00c5ec7c-c3ea-4a58-d7d2-8a2717bc8d35"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 215 entries, 0 to 214\n",
            "Data columns (total 14 columns):\n",
            " #   Column          Non-Null Count  Dtype  \n",
            "---  ------          --------------  -----  \n",
            " 0   sl_no           215 non-null    int64  \n",
            " 1   gender          215 non-null    object \n",
            " 2   ssc_p           215 non-null    float64\n",
            " 3   ssc_b           215 non-null    object \n",
            " 4   hsc_p           215 non-null    float64\n",
            " 5   hsc_b           215 non-null    object \n",
            " 6   hsc_s           215 non-null    object \n",
            " 7   degree_p        215 non-null    float64\n",
            " 8   degree_t        215 non-null    object \n",
            " 9   workex          215 non-null    object \n",
            " 10  etest_p         215 non-null    float64\n",
            " 11  specialisation  215 non-null    object \n",
            " 12  mba_p           215 non-null    float64\n",
            " 13  status          215 non-null    object \n",
            "dtypes: float64(5), int64(1), object(8)\n",
            "memory usage: 23.6+ KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "ENCODING THE CATEGORICAL VARIABLES"
      ],
      "metadata": {
        "id": "b60Hdn4Zb9B4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.preprocessing import LabelEncoder\n",
        "labels=LabelEncoder()\n",
        "\n",
        "dataset['gender']=labels.fit_transform(dataset['gender'])\n",
        "dataset['ssc_b']=labels.fit_transform(dataset['ssc_b'])\n",
        "dataset['hsc_b']=labels.fit_transform(dataset['hsc_b'])\n",
        "dataset['hsc_s']=labels.fit_transform(dataset['hsc_s'])\n",
        "dataset['degree_t']=labels.fit_transform(dataset['degree_t'])\n",
        "dataset['workex']=labels.fit_transform(dataset['workex'])\n",
        "dataset['specialisation']=labels.fit_transform(dataset['specialisation'])\n",
        "dataset['status']=labels.fit_transform(dataset['status'])"
      ],
      "metadata": {
        "id": "I-4rtFYBWkhG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "dataset"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 468
        },
        "id": "o-TPWecfW-_i",
        "outputId": "a9f1701c-26f7-454e-ffc4-2dfaf736a186"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "\n",
              "  <div id=\"df-0e18a2b2-f4a8-479b-8d64-4ed8b5f80a55\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>sl_no</th>\n",
              "      <th>gender</th>\n",
              "      <th>ssc_p</th>\n",
              "      <th>ssc_b</th>\n",
              "      <th>hsc_p</th>\n",
              "      <th>hsc_b</th>\n",
              "      <th>hsc_s</th>\n",
              "      <th>degree_p</th>\n",
              "      <th>degree_t</th>\n",
              "      <th>workex</th>\n",
              "      <th>etest_p</th>\n",
              "      <th>specialisation</th>\n",
              "      <th>mba_p</th>\n",
              "      <th>status</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>67.00</td>\n",
              "      <td>1</td>\n",
              "      <td>91.00</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>58.00</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>55.0</td>\n",
              "      <td>1</td>\n",
              "      <td>58.80</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>79.33</td>\n",
              "      <td>0</td>\n",
              "      <td>78.33</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>77.48</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>86.5</td>\n",
              "      <td>0</td>\n",
              "      <td>66.28</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>65.00</td>\n",
              "      <td>0</td>\n",
              "      <td>68.00</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>64.00</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>75.0</td>\n",
              "      <td>0</td>\n",
              "      <td>57.80</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>56.00</td>\n",
              "      <td>0</td>\n",
              "      <td>52.00</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>52.00</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>66.0</td>\n",
              "      <td>1</td>\n",
              "      <td>59.43</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>1</td>\n",
              "      <td>85.80</td>\n",
              "      <td>0</td>\n",
              "      <td>73.60</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>73.30</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>96.8</td>\n",
              "      <td>0</td>\n",
              "      <td>55.50</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>210</th>\n",
              "      <td>211</td>\n",
              "      <td>1</td>\n",
              "      <td>80.60</td>\n",
              "      <td>1</td>\n",
              "      <td>82.00</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>77.60</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>91.0</td>\n",
              "      <td>0</td>\n",
              "      <td>74.49</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>211</th>\n",
              "      <td>212</td>\n",
              "      <td>1</td>\n",
              "      <td>58.00</td>\n",
              "      <td>1</td>\n",
              "      <td>60.00</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>72.00</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>74.0</td>\n",
              "      <td>0</td>\n",
              "      <td>53.62</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>212</th>\n",
              "      <td>213</td>\n",
              "      <td>1</td>\n",
              "      <td>67.00</td>\n",
              "      <td>1</td>\n",
              "      <td>67.00</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>73.00</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>59.0</td>\n",
              "      <td>0</td>\n",
              "      <td>69.72</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>213</th>\n",
              "      <td>214</td>\n",
              "      <td>0</td>\n",
              "      <td>74.00</td>\n",
              "      <td>1</td>\n",
              "      <td>66.00</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>58.00</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>70.0</td>\n",
              "      <td>1</td>\n",
              "      <td>60.23</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>214</th>\n",
              "      <td>215</td>\n",
              "      <td>1</td>\n",
              "      <td>62.00</td>\n",
              "      <td>0</td>\n",
              "      <td>58.00</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>53.00</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>89.0</td>\n",
              "      <td>1</td>\n",
              "      <td>60.22</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>215 rows × 14 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-0e18a2b2-f4a8-479b-8d64-4ed8b5f80a55')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
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
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-0e18a2b2-f4a8-479b-8d64-4ed8b5f80a55 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-0e18a2b2-f4a8-479b-8d64-4ed8b5f80a55');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ],
            "text/plain": [
              "     sl_no  gender  ssc_p  ssc_b  ...  etest_p  specialisation  mba_p  status\n",
              "0        1       1  67.00      1  ...     55.0               1  58.80       1\n",
              "1        2       1  79.33      0  ...     86.5               0  66.28       1\n",
              "2        3       1  65.00      0  ...     75.0               0  57.80       1\n",
              "3        4       1  56.00      0  ...     66.0               1  59.43       0\n",
              "4        5       1  85.80      0  ...     96.8               0  55.50       1\n",
              "..     ...     ...    ...    ...  ...      ...             ...    ...     ...\n",
              "210    211       1  80.60      1  ...     91.0               0  74.49       1\n",
              "211    212       1  58.00      1  ...     74.0               0  53.62       1\n",
              "212    213       1  67.00      1  ...     59.0               0  69.72       1\n",
              "213    214       0  74.00      1  ...     70.0               1  60.23       1\n",
              "214    215       1  62.00      0  ...     89.0               1  60.22       0\n",
              "\n",
              "[215 rows x 14 columns]"
            ]
          },
          "metadata": {},
          "execution_count": 65
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X=dataset.drop(['status'], axis=1)\n",
        "Y=dataset['status']"
      ],
      "metadata": {
        "id": "EkCnNgdFXD9x"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "SPLITTING THE DATASET INTO THE TRAINING SET AND TESTING SET"
      ],
      "metadata": {
        "id": "radQsHLkcDqO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=.25, random_state=0)\n",
        "print(X_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jrY_esdzXPNH",
        "outputId": "b10706f7-8cef-4cbb-b7bc-634d4f98102b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "     sl_no  gender  ssc_p  ssc_b  ...  workex  etest_p  specialisation  mba_p\n",
            "138    139       0  82.00      1  ...       1    96.00               0  71.77\n",
            "52      53       0  40.89      1  ...       0    71.20               1  65.49\n",
            "66      67       1  83.00      1  ...       0    68.92               1  58.46\n",
            "26      27       1  71.00      1  ...       1    94.00               0  57.55\n",
            "61      62       1  84.20      0  ...       0    61.60               0  62.48\n",
            "..     ...     ...    ...    ...  ...     ...      ...             ...    ...\n",
            "67      68       1  80.92      1  ...       0    68.71               0  60.99\n",
            "192    193       1  65.20      0  ...       1    93.40               0  57.34\n",
            "117    118       1  77.00      1  ...       0    80.00               0  67.05\n",
            "47      48       1  63.00      0  ...       1    78.00               0  54.55\n",
            "172    173       1  73.00      1  ...       0    84.00               1  52.64\n",
            "\n",
            "[161 rows x 13 columns]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "thjv3a_4X0jq",
        "outputId": "a4aaa5f0-fa46-4698-8609-745c393d3356"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "138    1\n",
            "52     0\n",
            "66     1\n",
            "26     1\n",
            "61     1\n",
            "      ..\n",
            "67     1\n",
            "192    1\n",
            "117    1\n",
            "47     1\n",
            "172    1\n",
            "Name: status, Length: 161, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "TRAINING THE MODEL IN THE TRANING SET"
      ],
      "metadata": {
        "id": "7J1dMYefcKzY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.linear_model import LogisticRegression\n",
        "logreg= LogisticRegression(solver='liblinear')\n",
        "logreg"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PpsRHmOaYUSO",
        "outputId": "ea46d7fc-d3b1-49f6-eb67-dc0ae93a939c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LogisticRegression(solver='liblinear')"
            ]
          },
          "metadata": {},
          "execution_count": 70
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "logreg.fit(X_train, y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "a44h3CY8Yl6S",
        "outputId": "bf334a8a-9769-4690-e8dc-515ecc3b1b26"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LogisticRegression(solver='liblinear')"
            ]
          },
          "metadata": {},
          "execution_count": 71
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "PREDICTING THE MODEL IN THE TESTING SET"
      ],
      "metadata": {
        "id": "k23ojLVvcQF1"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "pred_train=logreg.predict(X_train)\n",
        "pred_train"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "prVfax-PY5-W",
        "outputId": "4f4fdd83-aa9c-47d2-90fe-035d8d47e05e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1,\n",
              "       1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1,\n",
              "       1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1,\n",
              "       1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0,\n",
              "       1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1,\n",
              "       1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0,\n",
              "       0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1,\n",
              "       1, 1, 1, 1, 1, 1, 1])"
            ]
          },
          "metadata": {},
          "execution_count": 72
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pred_test=logreg.predict(X_test)\n",
        "pred_test"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "g9AVeZ9UY9bP",
        "outputId": "804af11e-c859-4bf4-b2cb-0cd6f4beae06"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1,\n",
              "       1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1,\n",
              "       1, 1, 1, 1, 1, 1, 1, 1, 1, 1])"
            ]
          },
          "metadata": {},
          "execution_count": 74
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "MAKING CONFUSION MATRIX"
      ],
      "metadata": {
        "id": "4a9wvJlrcUT_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import confusion_matrix, accuracy_score,recall_score,roc_auc_score,precision_score,f1_score\n",
        "print(\"Test confusion matrix :\\n\",confusion_matrix(pred_test, y_test))\n",
        "print(\"Training Accuracy :\",accuracy_score(pred_train, y_train)*100)\n",
        "print(\"Test Accuracy :\",accuracy_score(pred_test, y_test)*100)\n",
        "print(\"Precision :\",precision_score(pred_test, y_test)*100)\n",
        "print(\"Recall :\",accuracy_score(pred_test, y_test)*100)\n",
        "print(\"F1-score\",f1_score(pred_test, y_test)*100)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Gw0k4IKDhv_z",
        "outputId": "f73686a1-e548-4258-e665-46592d7e9bf5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Test confusion matrix :\n",
            " [[10  3]\n",
            " [ 7 34]]\n",
            "Training Accuracy : 90.6832298136646\n",
            "Test Accuracy : 81.48148148148148\n",
            "Precision : 91.8918918918919\n",
            "Recall : 81.48148148148148\n",
            "F1-score 87.17948717948718\n"
          ]
        }
      ]
    }
  ]
}