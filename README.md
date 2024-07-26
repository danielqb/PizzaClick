# PizzaClick

PizzaClick is an intuitive and user-friendly application that simplifies the pizza ordering process. It allows users to fully customize their orders through a friendly interface. PizzaClick makes the pizza ordering experience efficient and enjoyable.

[![CodeQL](https://github.com/danielqb/PizzaClick/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/danielqb/PizzaClick/actions/workflows/github-code-scanning/codeql)
[![.github/workflows/docker-image.yml](https://github.com/danielqb/PizzaClick/actions/workflows/docker-image.yml/badge.svg)](https://github.com/danielqb/PizzaClick/actions/workflows/docker-image.yml)

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- Customize your pizza with various toppings
- User-friendly interface
- Real-time order tracking
- Secure payment options

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/danielqb/pizzaclick.git
    cd pizzaclick
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the development server:
    ```sh
    python manage.py runserver
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000/`.

## Development

To contribute to the development of PizzaClick, follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature/your-feature-name
    ```

3. Make your changes and commit them:
    ```sh
    git commit -m "Add your feature"
    ```

4. Push to the branch:
    ```sh
    git push origin feature/your-feature-name
    ```

5. Open a pull request.

## Deployment

### Docker

1. Build the Docker image:
    ```sh
    docker build -t pizzaclick .
    ```

2. Run the Docker container:
    ```sh
    docker run -d -p 8000:8000 pizzaclick
    ```

### Kubernetes

1. Apply the Kubernetes deployment:
    ```sh
    kubectl create namespace pizzaclick
    helm upgrade --install -n pizzaclick pizzaclick helm/
    ```

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact [your-email@example.com](mailto:your-email@example.com).

## Thanks
I would like to express my gratitude to the people who motivated me to undertake this challenge.
Thank you for your support and encouragement!