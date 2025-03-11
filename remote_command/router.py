import json
import re
import subprocess
import os
from datetime import datetime
from json import JSONDecodeError
from typing import Dict, Optional, List

from fastapi import APIRouter, HTTPException, Request, Header, Depends
from fastapi.responses import JSONResponse
from loguru import logger
from pydantic import BaseModel, Field, validator

router = APIRouter()


class CommandRequest(BaseModel):
    command: str = Field(..., description="Shell command to execute")
    timeout: Optional[int] = Field(30, description="Command execution timeout in seconds")


class CommandResponse(BaseModel):
    success: bool
    return_code: int
    stdout: str
    stderr: str
    timestamp: str
    execution_time: float


async def verify_api_key(authorization: str = Header(...)):
    try:
        # 从根目录加载API密钥
        with open("api_key.txt", "r") as f:
            api_key = f.read().strip()

        # 检查提供的密钥
        if authorization != f"Bearer {api_key}":
            logger.warning("Invalid API key used in request")
            raise HTTPException(status_code=401, detail="Invalid API key")

        return authorization
    except FileNotFoundError:
        logger.error("API key file not found")
        raise HTTPException(status_code=500, detail="API key configuration error")


@router.post("/run_command", response_model=CommandResponse)
async def run_command(command_request: CommandRequest, authorized: str = Depends(verify_api_key)):
    try:
        # 记录日志
        logger.info(f"Running command: {command_request.command}")

        # 记录开始时间
        start_time = datetime.now()

        # 执行命令并捕获输出
        result = subprocess.run(
            command_request.command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=command_request.timeout
        )

        # 计算执行时间
        execution_time = (datetime.now() - start_time).total_seconds()

        # 构建响应
        response = CommandResponse(
            success=result.returncode == 0,
            return_code=result.returncode,
            stdout=result.stdout,
            stderr=result.stderr,
            timestamp=datetime.now().isoformat(),
            execution_time=execution_time
        )

        return response

    except subprocess.TimeoutExpired:
        logger.error(f"Command execution timed out after {command_request.timeout} seconds")
        raise HTTPException(status_code=408,
                            detail=f"Command execution timed out after {command_request.timeout} seconds")
    except Exception as e:
        logger.error(f"Error executing command: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error executing command: {str(e)}")