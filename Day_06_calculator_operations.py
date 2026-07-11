{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOfYKMPxyDgTPHLa7nhhi/A",
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
        "<a href=\"https://colab.research.google.com/github/arpitabansal-compbio/30-Days-Of-Python/blob/main/Day_06_calculator_operations.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ufr2qKpclmlg",
        "outputId": "2b65f96b-b967-4b7c-afcd-227dde75c1f2"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--- CLINICAL DATA ENTRY CALCULATOR ---\n",
            "Enter cell count group A: 245\n",
            "Enter cell count group B: 155\n",
            "Total Combined Sample Count:\t400\n"
          ]
        }
      ],
      "source": [
        "# feat: implement basic clinical calculator for user inputs\n",
        "\n",
        "print(\"--- CLINICAL DATA ENTRY CALCULATOR ---\")\n",
        "\n",
        "# Step 1: Collect numbers from the user (arrives as text strings)\n",
        "raw_input_x = input(\"Enter cell count group A: \")\n",
        "raw_input_y = input(\"Enter cell count group B: \")\n",
        "\n",
        "# Step 2: Convert the text inputs into integers so we can do math\n",
        "count_x = int(raw_input_x)\n",
        "count_y = int(raw_input_y)\n",
        "\n",
        "# Step 3: Add the values together\n",
        "total_count = count_x + count_y\n",
        "\n",
        "# Step 4: Display the result cleanly using an f-string\n",
        "print(f\"Total Combined Sample Count:\\t{total_count}\")\n"
      ]
    }
  ]
}