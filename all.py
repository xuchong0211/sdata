import baostock as bs
import pandas as pd


def download_data(date):
    bs.login()

    #
    stock_rs = bs.query_all_stock(date)
    stock_df = stock_rs.get_data()
    data_df = pd.DataFrame()
    for code in stock_df["code"]:
        print("Downloading :" + code)
        k_rs = bs.query_history_k_data_plus(code, "date,code,open,high,low,close", date, date)
        data_df = data_df.append(k_rs.get_data())
    bs.logout()
    data_df.to_csv("~/20200610.DayData.csv", encoding="gbk", index=False)
    print(data_df)


# if __name__ == '__main__':
#
#     download_data("2019-02-25")
