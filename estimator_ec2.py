#!/usr/bin/env python3

from fastapi import FastAPI

import estimator_lambda
import uvicorn

app = FastAPI()


@app.get("/estimate")
async def estimate_endpoint(number_of_shots: int, reporting_rate: int):
    params = {"number_of_shots": number_of_shots, "reporting_rate": reporting_rate}
    return estimator_lambda.lambda_handler(params, None)


if __name__ == '__main__':
    uvicorn.run(app, port=80, host="0.0.0.0")
