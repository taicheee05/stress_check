import os

# プロジェクトのルートディレクトリ名
project_name = 'myproject'

# アプリケーション名
app_name = 'myapp'

# プロジェクトディレクトリのパス
project_dir = os.path.join(os.getcwd(), project_name)

# 作成するディレクトリのリスト
directories = [
    os.path.join(project_dir, app_name, 'migrations'),
    os.path.join(project_dir, app_name, 'templates', app_name),
    os.path.join(project_dir, 'static'),
    os.path.join(project_dir, 'media'),
]

# 作成するファイルのリスト
files = [
    os.path.join(project_dir, app_name, '__init__.py'),
    os.path.join(project_dir, app_name, 'admin.py'),
    os.path.join(project_dir, app_name, 'apps.py'),
    os.path.join(project_dir, app_name, 'forms.py'),
    os.path.join(project_dir, app_name, 'models.py'),
    os.path.join(project_dir, app_name, 'tests.py'),
    os.path.join(project_dir, app_name, 'views.py'),
    os.path.join(project_dir, app_name, 'migrations', '__init__.py'),
    os.path.join(project_dir, app_name, 'urls.py'),  # アプリケーション固有のURL設定
    os.path.join(project_dir, app_name, 'templates', app_name, 'survey.html'),
    os.path.join(project_dir, app_name, 'templates', app_name, 'results.html'),
]

# ディレクトリ作成
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# 空のファイル作成
for file in files:
    with open(file, 'a') as f:
        pass  # ファイルが存在しない場合は作成し、存在する場合は何もしない

print(f'{project_name} プロジェクト内の {app_name} アプリケーションのフォルダとファイルの作成が完了しました。')
