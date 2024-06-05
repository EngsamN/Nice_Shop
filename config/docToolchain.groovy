docToolchain {
    inputPath = 'src/docs'
    outputPath = 'build/docs'
    pdfOutput = 'build/docs/pdf'
    htmlOutput = 'build/docs/html5'

    // Add your project-specific configurations here
    includeTopics = ['00-introduction', '01-architecture_overview', '02-concepts']
}

templates {
    // Specify any templates you want to use
    html {
        basedir = 'templates/html'
    }
}
