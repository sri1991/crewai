# Healthcare Management System

Welcome to the Healthcare Management System, powered by [crewAI](https://crewai.com). This project implements a multi-agent AI system for comprehensive healthcare management, leveraging crewAI's framework to coordinate multiple specialized healthcare agents for patient care and support.

## System Overview

The system consists of three specialized AI agents:

1. **Medication Management Agent**
   - Medication tracking and scheduling
   - Adherence monitoring
   - Medication information and alerts
   - Side effects and interactions tracking

2. **Appointment Scheduling Agent**
   - Doctor appointment management
   - Provider matching
   - Scheduling automation
   - Follow-up coordination

3. **Health Tips and Advice Agent**
   - Personalized health recommendations
   - Progress tracking
   - Lifestyle guidance
   - Health data analysis

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling.

First, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

```bash
crewai install
```

### Configuration

1. Add your `GOOGLE_API_KEY` to the `.env` file
2. Configure agents in `src/healthcare/config/agents.yaml`
3. Define tasks in `src/healthcare/config/tasks.yaml`
4. Customize logic in `src/healthcare/crew.py`
5. Modify inputs in `src/healthcare/main.py`

## Running the System

To start the healthcare management system:

```bash
$ crewai run
```

This command initializes all healthcare agents and begins their respective tasks according to your configuration.

## Project Structure

```
healthcare/
├── src/
│   └── healthcare/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       ├── crew.py
│       └── main.py
├── .env
└── README.md
```

## Security and Privacy

This system is designed with healthcare data privacy in mind:
- Encrypted data storage
- HIPAA-compliant communication
- Secure authentication
- Privacy-first data handling

## Support

For support and assistance:
- Visit [crewAI documentation](https://docs.crewai.com)
- Submit issues on [GitHub](https://github.com/joaomdmoura/crewai)
- Join the [Discord community](https://discord.com/invite/X4JWnZnxPb)
- [Chat with documentation](https://chatg.pt/DWjSBZn)

## Contributing

We welcome contributions to improve the healthcare management system. Please follow our contribution guidelines and maintain HIPAA compliance in all modifications. 