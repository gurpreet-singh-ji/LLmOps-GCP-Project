import operator
from typing import TypedDict, Annotated, List, Optional,Dict,Any

class VideoErrorReport(TypedDict):
    category:str
    desc:str
    level:str
    timestamp: Optional[str]

class VideoState(TypedDict):
    video_url: str
    video_id: str
    local_file_path: Optional[str]
    video_metadata: Dict[str,Any]
    ocr_text: List[str]
    errorResult: Annotated[List[VideoErrorReport], operator.add]
    finalStatus: str
    finalReport: str
    