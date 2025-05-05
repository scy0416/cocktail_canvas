pipeline {
  agent any

  environment {
    COMPOSE_PROJECT_DIR = "${WORKSPACE}"
  }

  stages {
    stage('Checkout') {
      steps {
        // master 브랜치 당겨오기
        checkout([
          $class: 'GitSCM',
          branches: [[name: '*/master']],
          userRemoteConfigs: [[
            url: 'https://github.com/scy0416/cocktail_canvas.git',
            credentialsId: 'github-pat'
          ]]
        ])
      }
    }

    stage('Deploy with Docker Compose') {
      steps {
        dir("${COMPOSE_PROJECT_DIR}") {
          // 이미지 최신화
          sh 'docker compose pull'
          // 백그라운드 재배포(재빌드 포함)
          sh 'docker compose -f docker-compose.prod.yaml up -d --build'
        }
      }
    }
  }

  post {
    success {
      echo "✅ 배포 성공"
    }
    failure {
      echo "❌ 배포 실패"
    }
  }
}
