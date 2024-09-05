from graphviz import Digraph

def create_music_streaming_cicd_diagram():
    dot = Digraph(comment='Music Streaming App CI/CD Pipeline')
    dot.attr(rankdir='TB', size='15,15')

    # CI/CD Pipeline
    with dot.subgraph(name='cluster_cicd') as c:
        c.attr(label='CI/CD Pipeline')
        c.node('git', 'Git Repository')
        c.node('jenkins', 'Jenkins')
        c.node('build', 'Build')
        c.node('unit_tests', 'Unit Tests')
        c.node('sonarqube', 'SonarQube\nCode Analysis')
        c.node('integration_tests', 'Integration Tests')
        c.node('nexus', 'Nexus\nArtifact Repository')
        c.node('test_deploy', 'Deploy to Test')
        c.node('functional_tests', 'Functional Tests')
        c.node('prod_deploy', 'Deploy to Production')

    # Monitoring
    dot.node('grafana', 'Grafana\nMonitoring')

    # Environments
    dot.node('test_env', 'Test Environment')
    dot.node('prod_env', 'Production Environment')

    # Define edges
    dot.edge('git', 'jenkins')
    dot.edge('jenkins', 'build')
    dot.edge('build', 'unit_tests')
    dot.edge('unit_tests', 'sonarqube')
    dot.edge('sonarqube', 'integration_tests')
    dot.edge('integration_tests', 'nexus')
    dot.edge('nexus', 'test_deploy')
    dot.edge('test_deploy', 'test_env')
    dot.edge('test_env', 'functional_tests')
    dot.edge('functional_tests', 'prod_deploy')
    dot.edge('prod_deploy', 'prod_env')
    dot.edge('prod_env', 'grafana')

    # Render the diagram
    dot.render('music_streaming_cicd_pipeline', format='png', cleanup=True)
    print("Diagram created: music_streaming_cicd_pipeline.png")

if __name__ == "__main__":
    create_music_streaming_cicd_diagram()