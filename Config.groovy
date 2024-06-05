docToolchain {
    inputPath = 'src/docs/asciidoc'
    outputPath = 'build/docs'
    pdfOutput = 'build/docs/pdf'
    htmlOutput = 'build/docs/html5'

    includeTopics = [
        '01_introduction_and_goals',
        '02_architecture_constraints',
        '03_context_and_scope',
        '04_solution_strategy',
        '05_building_block_view',
        '06_runtime_view',
        '07_deployment_view',
        '08_concepts',
        '09_architecture_decisions',
        '10_quality_requirements',
        '11_technical_risks',
        '12_glossary'
    ]
}
