import pandas as pd
import pd_settings

# This class decodes a plottable message that's represented in a url document's table
# Author: Daniel Oyebolu -> linkedin.com/daniel-oyebolu
class GridCodeDecoder:

    # A method that:
    # a. prepares and cleans the data table.
    # b. constructs the code/message/image's list
    # c. maps and presents the message
    #
    # external framework used: pandas
    def construct_message(self, url):
        tables = pd.read_html(
            url,
            header=0,
            flavor='html5lib'
        )

        df = tables[0]

        # replacing null values with a space character
        df['Character'] = df['Character'].fillna(" ")

        df.sort_values(['y-coordinate', 'x-coordinate'], ascending=[True, True], inplace=True)
        # resetting index
        df.reset_index(drop=True, inplace=True)

        df=df[['y-coordinate', 'x-coordinate', 'Character']]

        print(df.head(1000))

        # code/message/image (x and y-axis) as a list
        code_list=self.construct_code_list(df)

        # presenting the message
        for plot_row in code_list:
            print("".join(plot_row))



    # A function that constructs the code/message/image's list
    def construct_code_list(self, dataframe):

        # list that holds the decoded message
        code_list = []

        # populating the code/message/image's list
        for i in range(len(dataframe)):
            character_details = dataframe.iloc[i]
            # print(character_details)


            y_value = int(character_details['y-coordinate'])
            x_value = int(character_details['x-coordinate'])
            code = character_details['Character']

            if y_value > len(code_list) - 1:
                code_list.insert(y_value, [])

            code_list[y_value].insert(x_value, code)
            # print(code_list)

        # reversing the code/message/image's list to represent the y-axis correctly i.e in descending order, top to bottom
        code_list.reverse()

        return code_list


grid_code_decoder=GridCodeDecoder()
grid_code_decoder.construct_message(
    "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
    # "https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub"
)