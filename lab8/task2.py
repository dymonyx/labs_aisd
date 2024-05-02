import aiohttp
import asyncio

class GitHubApiClient:
    def __init__(self, access_token):
        self.base_url = 'https://api.github.com/'
        self.access_token = access_token

    async def get_user_repos(self, username):
        async with aiohttp.ClientSession() as session:
            headers = {
                'Authorization': f'token {self.access_token}'
            }
            async with session.get(f'{self.base_url}users/{username}/repos', headers=headers) as response:
                data = await response.json()
                return data

async def fetch_user_repos(client, username):
    user_repos = await client.get_user_repos(username)
    return username, user_repos

async def main():
    access_token = ''
    usernames = ['nonezonyx', 'dymonyx', 'john-preston']

    client = GitHubApiClient(access_token)

    tasks = [fetch_user_repos(client, username) for username in usernames]
    results = await asyncio.gather(*tasks)

    for username, repos in results:
        print(f"Repos for {username}:")
        for repo in repos[-5:]:
            print(f"name: {repo['name']}, node_id: {repo['node_id']}")
        print("\n")

if __name__ == '__main__':
    asyncio.run(main())
