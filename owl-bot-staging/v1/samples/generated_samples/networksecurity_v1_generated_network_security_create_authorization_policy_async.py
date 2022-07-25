# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for CreateAuthorizationPolicy
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-networksecurity


# [START networksecurity_v1_generated_NetworkSecurity_CreateAuthorizationPolicy_async]
from google.cloud import networksecurity_v1


async def sample_create_authorization_policy():
    # Create a client
    client = networksecurity_v1.NetworkSecurityAsyncClient()

    # Initialize request argument(s)
    authorization_policy = networksecurity_v1.AuthorizationPolicy()
    authorization_policy.name = "name_value"
    authorization_policy.action = "DENY"

    request = networksecurity_v1.CreateAuthorizationPolicyRequest(
        parent="parent_value",
        authorization_policy_id="authorization_policy_id_value",
        authorization_policy=authorization_policy,
    )

    # Make the request
    operation = client.create_authorization_policy(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)

# [END networksecurity_v1_generated_NetworkSecurity_CreateAuthorizationPolicy_async]