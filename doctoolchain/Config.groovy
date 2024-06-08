// Path where the docToolchain will search for the input files.
inputPath = 'src/docs/asciidoc'

// Path where the generated documentation will be placed.
outputPath = 'build/docs'

// Define the input files and formats
inputFiles = [
    [file: 'index.adoc', formats: ['html', 'pdf']]
]

// Folders where asciidoc will find images.
// These will be copied as resources to ./images
// Folders are relative to inputPath
imageDirs = []

// Task input directories and files
taskInputsDirs = ["${inputPath}/images"]
taskInputsFiles = []

// Configuration for exportChangelog
exportChangelog = [:]

changelog.with {
    dir = 'src/docs'
    cmd = 'git log --pretty=format:%x7c%x20%ad%x20%n%x7c%x20%an%x20%n%x7c%x20%s%x20%n --date=short'
}

// Configuration for publishToConfluence
confluence = [:]

confluence.with {
    input = [
        [ file: "build/docs/html5/arc42-template-de.html" ],
    ]
    api = 'https://[yourServer]/[context]/rest/api/'
    spaceKey = 'asciidoc'
    preambleTitle = ''
    createSubpages = false
    pagePrefix = ''
    pageSuffix = ''
}
