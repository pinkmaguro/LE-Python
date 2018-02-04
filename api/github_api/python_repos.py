import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


def get_reponse():
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    req = requests.get(url)
    return req

def get_repo_dicts(response):
    """Return a set of dicts representing the most popular repositories."""
    response_dict = response.json()
    repo_dicts = response_dict['items']
    return repo_dicts

def get_names_plot_dicts(repo_dicts):
    """그래프를 그리기위한 데이터 수집"""
    names, plot_dicts = [], []
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])

        # Some projects lack a description, which causes an error when 
        #  labeling bars. Specify a label if there's no description.
        description = repo_dict['description']
        if not description:
            description = "No description provided."

        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': description,
            'xlink': repo_dict['html_url'],
            }
        plot_dicts.append(plot_dict)
    return names, plot_dicts

def make_visulization(names, plot_dicts):
    my_style = LS('#333366', base_style=LCS)
    my_style.title_font_size = 24
    my_style.label_font_size = 14
    my_style.major_label_font_size = 18

    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000

    chart = pygal.Bar(my_config, style=my_style)
    chart.title = 'Most-Starred Python Projects on GitHub'
    chart.x_labels = names

    chart.add('', plot_dicts)
    chart.render_to_file('python_repos.svg')


def main():
    print('strat')
    # 깃헙의 파이썬 리포중 스타를 많이 받은 순서대로 나열한 json
    # 현재 2백만개나 있다.
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    req = requests.get(url)
    print(type(req))

    response_dict = req.json()
    print("Total repositories: ", response_dict['total_count'])

    print("Status code: ", req.status_code)

    # API로 받은 자료 중에서 저장소 정보를 확인
    repo_dicts = response_dict['items']
    print("Repositories returned: ", len(repo_dicts))

    # 첫 번째 저장소 확인
    # 70 개의 key 가 있다.
    repo_dict = repo_dicts[0]
    print('Keys: ', len(repo_dict))
    for key in sorted(repo_dict.keys()):
        print(key)

    print('First repository')
    print('Name: ', repo_dict['name'])
    print('Stars: ', repo_dict['stargazers_count'])
    print('Repository: ', repo_dict['html_url'])
    print('Created: ', repo_dict['created_at'])
    print('Description: ', repo_dict['description'])

    
    # 시각화 준비
    names, plot_dicts = [], []
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])

        description = repo_dict['description']
        if not description:
            description = 'No description provided.'

        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': description,
            'xlink': repo_dict['html_url']
        }
        plot_dicts.append(plot_dict)


    # 시각화
    my_style = LS('#333366', base_style=LCS) # 짙은 파란색
    my_style.title_font_size = 24
    my_style.label_font_size = 14
    my_style.major_label_font_size = 18

    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000

    chart = pygal.Bar(style=my_style)
    chart.title = 'Most-Starred Python Projects on GitHub'
    chart.x_labels = names

    chart.add('', plot_dicts)
    chart.render_to_file('python_repos.svg')

    

if __name__ == '__main__':
    main()