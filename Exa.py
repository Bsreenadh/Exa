from exa_py import Exa
exa = Exa ("Enter your Api key here")
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

