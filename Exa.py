from exa_py import Exa
exa = Exa ("74d179aa-2e8f-43f6-853e-424a92990fa6")
query = input('Search here: ')
response = exa.search(
  query,
  num_results=5,
  type='keyword',
  include_domains=['https://www.instagram.com'],
    use_autoprompt=True,
)

for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print(response)

