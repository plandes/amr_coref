# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).


## [Unreleased]


## [0.0.2] - 2023-12-10
### Changed
- Fix multiprocessing resource leak.  This happens when an exception is raised
  and the multiprocessing pool (or thread pool) is not closed.
- Fix torch `torch.utils.data.Sampler` taking a `data_source` as the
  initializer.


## [0.0.1] - 2023-12-10
### Added
- Initial version forked from the [amr_coref] project by Brad Jascob.


<!-- links -->
[Unreleased]: https://github.com/plandes/amr_coref/compare/v0.0.2...HEAD
[0.0.2]: https://github.com/plandes/amr_coref/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/plandes/amr_coref/compare/v0.0.0...v0.0.1

[amr_coref]: https://github.com/bjascob/amr_coref
