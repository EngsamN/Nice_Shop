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
