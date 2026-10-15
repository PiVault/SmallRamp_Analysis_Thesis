"""Project path configuration.

Import ``paths`` wherever project-root-relative paths are needed::

    from src.config import paths
    metadata = bp.get_metadata(paths=paths)

``Path(__file__)`` is immune to changes in the kernel working directory,
so this is safe to import from any notebook regardless of where it was opened.
"""
from pathlib import Path
import balancepy.anaropia_project as bpap

PROJECT_ROOT = Path(__file__).parent.parent.resolve()
paths = bpap.ProjectPaths(project_root=PROJECT_ROOT)

## Override paths for alternative data organization
## This is optional and can be customized as needed. The example below assumes an
## alternative data organization under "data_alt" and results under "results_alt".
#
# paths = bpap.ProjectPaths(
#     project_root=PROJECT_ROOT,
#     data_raw_override=PROJECT_ROOT / "data_alt" / "raw",
#     metadata_override=PROJECT_ROOT / "data_alt" / "metadata.xlsx",
#     quality_flags_override=PROJECT_ROOT / "data_alt" / "quality_flags.csv",
#     processed_dir_override=PROJECT_ROOT / "data_alt" / "processed" / "sr_data",
#     datacheck_plots_override=PROJECT_ROOT / "results_alt" / "datacheck_plots",
#     csmi_plots_override=PROJECT_ROOT / "results_alt" / "csmi_plots",
# )
