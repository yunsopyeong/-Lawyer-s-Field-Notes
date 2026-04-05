import json
import os
import sys
from pathlib import Path

import requests


def main() -> None:
    if len(sys.argv) != 5:
        print("사용법:")
        print("python tools/send_project_result.py <owner> <repo> <title> <file_path>")
        sys.exit(1)

    owner, repo, title, file_path = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    token = os.getenv("GITHUB_TOKEN")

    if not token:
        print("환경변수 GITHUB_TOKEN 이 필요합니다.")
        sys.exit(1)

    content_path = Path(file_path)
    if not content_path.exists():
        print(f"파일이 없습니다: {file_path}")
        sys.exit(1)

    content = content_path.read_text(encoding="utf-8")
    target_path = f"incoming/{content_path.name}"

    url = f"https://api.github.com/repos/{owner}/{repo}/dispatches"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    payload = {
        "event_type": "project_result_publish",
        "client_payload": {
            "title": title,
            "path": target_path,
            "content": content,
            "base_branch": "main",
        },
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=30)
    print("status:", response.status_code)
    if response.text:
        print(response.text)


if __name__ == "__main__":
    main()
