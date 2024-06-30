import org.gradle.api.tasks.Exec

project.ext {
    inputPath = './source'
    outputPath = './build/docs'
}

task generateSphinxDocs(type: Exec) {
    commandLine 'make', 'html'
    workingDir project.inputPath
}

task generateSite {
    dependsOn generateSphinxDocs
    doLast {
        println "Site generation complete."
    }
}
// generateOpenApiDocs {
//     inputFile = '../.github/workflows/openapi.yaml'
//     outputDir = 'build/api-docs'
//     config = [
//         format: 'html'
//     ]
// }
