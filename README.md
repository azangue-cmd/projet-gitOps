# projet-gitOps

Automated GitOps platform integrating DevSecOps practices and Artificial Intelligence for continuous security analysis.

## Stack
- Docker for packaging the application
- Kubernetes (k3s-compatible manifests) for deployment
- ArgoCD for GitOps continuous reconciliation
- GitHub Actions for CI and security scanning
- AI remediation module for automated vulnerability fix suggestions

## Repository structure
- `app/`: minimal application exposing `/health`
- `ai/remediate.py`: transforms scanner findings into remediation suggestions
- `infra/k8s/base/`: Kubernetes deployment and service manifests
- `infra/argocd/application.yaml`: ArgoCD application declaration
- `.github/workflows/`: CI + scheduled AI remediation workflows

## Local validation
```bash
python -m py_compile app/main.py ai/remediate.py
docker build -t local/gitops-app:test .
```

## k3s + ArgoCD GitOps flow
1. Install k3s and ArgoCD in your cluster.
2. Apply `infra/argocd/application.yaml`.
3. ArgoCD continuously syncs `infra/k8s/base/` from this repository.
4. CI runs syntax checks, image build, and Trivy security scan.
5. Scheduled/triggered AI remediation workflow parses vulnerability findings and emits fix suggestions.
