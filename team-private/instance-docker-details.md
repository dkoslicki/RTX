# NCATS-supplied EC2 instance

- hostname: `lysine.ncats.io`
- username: `admin`
- authentication: using `id_rsa.pub` (ask Steve if you do not have `ssh` access)
- host OS: Debian 4.9.51-1
- NOTE: use of this EC2 instance is subject to some additional caveats and
restrictions because it is provided by the United States Government and the
National Institutes of Health; see the `/etc/issue` file
- Docker container: `NCATS3`
- Docker container run command: see `run_container_lysine.ncats.io.sh`

# Oregon State Univ.-supplied EC2 instance

- hostname: `ncats.saramsey.org`
- username: `ubuntu`
- authentication: using `id_rsa.pub`  (ask Steve if you do not have `ssh` access)
- host OSU: Ubuntu 16.04
- Docker container: `ncats`
- Docker container run command: see `run_container_ncats.saramsey.org.sh`
