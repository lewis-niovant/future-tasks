# FutureTasks.app

## Overview

FutureTasks.app is an interactive research tool analyzing AI's potential impact on occupational tasks in the UK labour market. Built as part of MSc Applied Economics research at Strathclyde University (2024), this platform evaluates over 75,000 task-occupation pairs using GPT-4o to assess how artificial intelligence may affect different tasks within occupations.

## Methodology

### Data Sources
- **UK SOC 2020**: Standard Occupational Classification codes and descriptions
- **O*NET Database**: Task descriptions and occupational characteristics mapped to UK occupations
- **GPT-4o**: Systematic task evaluations using advanced language models
- **Economic Indicators**: UK wage and employment data
- **Anthropic Economic Index**: Task mappings and automation vs. augmentation patterns

### Anthropic Data Integration
This research builds upon Anthropic's Economic Index methodology ([paper](https://assets.anthropic.com/m/2e23255f1e84ca97/original/Economic_Tasks_AI_Paper.pdf)), incorporating:
- Task-level analysis patterns from millions of Claude conversations
- Automation vs. augmentation interaction frameworks
- O*NET task mappings and occupational categorizations
- Wage and employment correlations with AI exposure

The methodology extends Anthropic's approach by:
1. Adapting task classifications for the UK labor market
2. Implementing a scenario-based analysis framework
3. Developing a 14-step evaluation questionnaire
4. Integrating UK-specific economic indicators

### Classification Framework
Tasks are evaluated through a 14-step questionnaire and classified into:

1. **Human-Only Tasks**: Requiring physical presence, complex judgment, or facing regulatory barriers
2. **AI-Assisted Tasks**: Where AI augments human capabilities
3. **AI-Automated Tasks**: Potentially automatable with minimal human oversight

### AI Capability Scenarios
The analysis considers three scenarios:

1. **Current Capabilities (Limited Integration)**
   - Present-day AI capabilities
   - Basic tasks: reading comprehension, summarization
   - Integration limited by cost, security concerns

2. **Enhanced Capabilities (Moderate Integration)**
   - Near-future capabilities (2-5 years)
   - Advanced tasks: legal reasoning, multimodal processing
   - Improved but not complete organizational integration

3. **Advanced Capabilities (Widespread Integration)**
   - Long-term potential (5-10 years)
   - Complex tasks: advanced reasoning, creative generation
   - Widespread adoption across industries

## Technical Implementation

### Stack
- **Backend**: Python/Flask RESTful API
- **Frontend**: HTML/JavaScript/CSS with responsive design
- **Data Processing**: Pandas, NumPy for statistical analysis
- **AI Integration**: GPT-4o for natural language processing
- **Deployment**: Replit cloud platform

### Project Structure
```
├── src/
│   ├── api/
│   │   └── app.py              # Flask application & API endpoints
│   └── core/
│       └── data_processing.py  # Data processing & analysis logic
├── static/
│   ├── css/                    # Stylesheets
│   ├── js/                     # Frontend JavaScript
│   └── images/                 # Static images
├── templates/                  # HTML templates
├── requirements.txt            # Python dependencies
└── README.md                  # Project documentation
```

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/futuretasks-app.git
cd futuretasks-app
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Run the application
```bash
python src/api/app.py
```

## Data Sources & Attribution

### O*NET Database
- Source: [O*NET Resource Center](https://www.onetcenter.org/)
- Usage: Task descriptions and occupational characteristics
- License: Public Domain

### UK SOC 2020
- Source: [Office for National Statistics](https://www.ons.gov.uk/)
- Usage: Occupational classifications and descriptions
- License: Open Government License v3.0

### Anthropic Economic Index
- Source: [Anthropic](https://www.anthropic.com/news/the-anthropic-economic-index)
- Usage: Task mappings and automation patterns
- License: CC-BY

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, contact: lewis@niovant.com

## Author

**Lewis O'Neill**  
Founder & CEO, Niovant (AI Research & Development)  
MSc Applied Economics, Strathclyde University (2024) 