import json
import sys

class NemeanParser():

	def __init__(self):
		self.input_handle=sys.argv[1]
		self.reader=open(self.input_handle,'r').read()
		self.ifile=json.loads(self.reader.decode('string_escape'))
		self.length=int(self.ifile['num_company_results'])
		self.bond_yield_1962=4.4
		self.bond_yield_current=4.58
		self.results={}
		self.output_file=open('/var/www/html/ans','w')
		self.column_idx={'market_cap':0,
				'price_per_earnings':1,
				'dividend_yield':2,
				'price_to_book':3,
				'current_ratio':4,
				'debt_equity':5,
				'profit_margin':6,
				'growth':7,
				'eps':8,
				'price':9,
				}

	def parse(self):
		for i in range(self.length):
			stock=self.ifile['searchresults'][i]
			title=stock['title']
			ticker=stock['ticker']
			columns=stock['columns']
			market_cap=columns[self.column_idx['market_cap']]['value']
			price_per_earnings=columns[self.column_idx['price_per_earnings']]['value']
			dividend_yield=columns[self.column_idx['dividend_yield']]['value']
			price_to_book=columns[self.column_idx['price_to_book']]['value']
			current_ratio=columns[self.column_idx['current_ratio']]['value']
			debt_equity=columns[self.column_idx['debt_equity']]['value']
			profit_margin=columns[self.column_idx['profit_margin']]['value']
			growth=columns[self.column_idx['growth']]['value']
			eps=columns[self.column_idx['eps']]['value']
			price=columns[self.column_idx['price']]['value']
			try:
				profit_margin,dividend_yield,price_to_book,eps,growth,price_per_earnings=map(float,[profit_margin,dividend_yield,price_to_book,eps,growth,price_per_earnings])
			except ValueError:
				continue

			ib=self.intrinsic_Buffett(profit_margin,dividend_yield,price_to_book)
			ig=self.intrinsic_Graham(eps,growth)
			ia=self.intrinsic_alternative(price_to_book,price_per_earnings)
			self.results[ticker]={'title':title,'ticker':ticker,'profit_margin':profit_margin,'debt_equity':debt_equity,'ib':ib,'ia':ia,'ig':ig,'price':price}
		self.output_file.write("var s=%s"%(json.dumps(self.results)))
		#print(self.results)
				



        def intrinsic_Buffett(self,net_profit,dividend_yield,price_to_book):
                #multiple of 10
                return "%.2f"%((net_profit+dividend_yield)/price_to_book)

        def intrinsic_Graham(self,eps,growth):
                #estimated future value
                return "%.2f"%((eps*(8.5+(2*growth))*self.bond_yield_1962)/self.bond_yield_current)

        def intrinsic_alternative(self,price_to_book,price_per_earnings):
                #Want less than 22
                return "%.2f"%(price_to_book*price_per_earnings)
        
	


_=NemeanParser()
_.parse()

