{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNuQlDiyw17LL27uAYyVxQU",
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
        "<a href=\"https://colab.research.google.com/github/arpitabansal-compbio/30-Days-Of-Python/blob/main/day_04_dashboard.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8lCJ4HNOjuRL",
        "outputId": "39a14f1b-8461-427a-fabd-0d005f658a5f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your name: ARPITA BANSAL \n",
            "\n",
            "=====================================\n",
            "    DELHI GENOMICS RESEARCH LAB\n",
            "=====================================\n",
            "Investigator:  ARPITA BANSAL \n",
            "Sample ID:     DL-2026-X9\n",
            "Total Bases:   1550 str\n",
            "Status:        Staged for Sequence\n",
            "=====================================\n",
            "\n"
          ]
        }
      ],
      "source": [
        "# Day 4: Clinical Laboratory Dashboard Setup\n",
        "# Tracking patient data using clean f-string blocks\n",
        "\n",
        "# 1. Input variables for the Delhi clinical lab\n",
        "investigator = input(\"Enter your name: \")\n",
        "sample_id = \"DL-2026-X9\"\n",
        "base_pairs = 1550\n",
        "\n",
        "# 2. Production-grade triple quote template block\n",
        "dashboard = f\"\"\"\n",
        "=====================================\n",
        "    DELHI GENOMICS RESEARCH LAB\n",
        "=====================================\n",
        "Investigator:  {investigator}\n",
        "Sample ID:     {sample_id}\n",
        "Total Bases:   {base_pairs} str\n",
        "Status:        Staged for Sequence\n",
        "=====================================\n",
        "\"\"\"\n",
        "\n",
        "print(dashboard)\n"
      ]
    }
  ]
}