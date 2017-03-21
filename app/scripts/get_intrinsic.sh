#!/bin/bash
base=$1
if [[ -z $base ]]
then
echo "Please provide base path"
usage
exit 1
fi

usage(){
echo "./get_intrinsic.sh base_path"
}

wget "https://www.google.com/finance?start=0&num=3000&q=%5Bcurrency%20%3D%3D%20%22USD%22%20%26%20((exchange%20%3D%3D%20%22OTCMKTS%22)%20%7C%20(exchange%20%3D%3D%20%22OTCBB%22)%20%7C%20(exchange%20%3D%3D%20%22NYSEMKT%22)%20%7C%20(exchange%20%3D%3D%20%22NYSEARCA%22)%20%7C%20(exchange%20%3D%3D%20%22NYSE%22)%20%7C%20(exchange%20%3D%3D%20%22NASDAQ%22))%20%26%20(market_cap%20%3E%3D%200)%20%26%20(market_cap%20%3C%3D%20587960000000)%20%26%20(pe_ratio%20%3E%3D%200)%20%26%20(pe_ratio%20%3C%3D%2015)%20%26%20(dividend_yield%20%3E%3D%200)%20%26%20(dividend_yield%20%3C%3D%20800001)%20%26%20(price_to_book%20%3E%3D%200)%20%26%20(price_to_book%20%3C%3D%202)%20%26%20(current_assets_to_liabilities_ratio_year%20%3E%3D%202)%20%26%20(current_assets_to_liabilities_ratio_year%20%3C%3D%204698)%20%26%20(total_debt_to_equity_year%20%3E%3D%20-12.6)%20%26%20(total_debt_to_equity_year%20%3C%3D%2030)%20%26%20(net_profit_margin_percent_trailing_12months%20%3E%3D%20-7680000)%20%26%20(net_profit_margin_percent_trailing_12months%20%3C%3D%20531836)%20%26%20(net_income_growth_rate_5years%20%3E%3D%20-81.93)%20%26%20(net_income_growth_rate_5years%20%3C%3D%20497)%20%26%20(earnings_per_share%20%3E%3D%20-76560000)%20%26%20(earnings_per_share%20%3C%3D%2088350000)%20%26%20(last_price%20%3E%3D%200)%20%26%20(last_price%20%3C%3D%20218011)%5D&restype=company&output=json&noIL=1&ei=uNOmV6AfkYOYAbCripgM" -O $base/input/input_file

sed -i '/^\"original_query/d' $base/input/input_file
sed -i '/^\"query_for_display/d' $base/input/input_file
python $base/scripts/parser.py $base/input/input_file
