#!/usr/bin/env python
"""
CloudGenix Python SDK - PUT

**Author:** CloudGenix

**Copyright:** (c) 2017-2021 CloudGenix, Inc

**License:** MIT
"""
import logging

__author__ = "CloudGenix Developer Support <developers@cloudgenix.com>"
__email__ = "developers@cloudgenix.com"
__copyright__ = "Copyright (c) 2017-2021 CloudGenix, Inc"
__license__ = """
    MIT License

    Copyright (c) 2017-2021 CloudGenix, Inc

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

# Set logging to function name
api_logger = logging.getLogger(__name__)
"""logging.getlogger object to enable debug printing via `cloudgenix.API.set_debug`"""


class Put(object):
    """
    CloudGenix API - PUT requests

    Object to handle making Put requests via shared Requests Session.
    """

    # placeholder for parent class namespace
    _parent_class = None

    def access_elementusers(self, elementuser_id, access_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update an existing element user access.

          **Parameters:**:

          - **elementuser_id**: Element User ID
          - **access_id**: Access ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **element_id:**  Type: string 
           - **role:**  Type: string 
           - **tenant_id:**  Type: string 
           - **user_id:**  Type: string 

          **Required Attributes:** ['element_id', 'id', 'role', 'tenant_id', 'user_id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elementusers/{}/access/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    elementuser_id,
                                                                                    access_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def appdefs(self, appdef_id, data, tenant_id=None, api_version="v2.3"):
        """
        Update a application definition

          **Parameters:**:

          - **appdef_id**: Application Definition ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.3)

          **Payload Attributes:** 

           - **abbreviation:**  Type: string 
           - **aggregate_flows:**  Type: boolean 
           - **app_type:**  Type: string 
           - **app_unreachability_detection:**  Type: boolean 
           - **category:**  Type: string 
           - **conn_idle_timeout:**  Type: integer 
           - **description:**  Type: string 
           - **display_name:**  Type: string 
           - **domains:**  [Type: string] 
           - **ingress_traffic_pct:**  Type: integer 
           - **ip_rules:**  [Type: u] 
           - **is_deprecated:**  Type: boolean 
           - **network_scan_application:**  Type: boolean 
           - **order_number:**  Type: integer 
           - **overrides_allowed:**  Type: boolean 
           - **parent_id:**  Type: string 
           - **path_affinity:**  Type: string 
           - **session_timeout:**  Type: integer 
           - **system_app_overridden:**  Type: boolean 
           - **tags:**  [Type: string] 
           - **tcp_rules:**  [Type: s] 
           - **transfer_type:**  Type: string 
           - **udp_rules:**  [Type: t] 
           - **use_parentapp_network_policy:**  Type: boolean 

          **Required Attributes:** ['aggregate_flows', 'app_type', 'app_unreachability_detection', 'category', 'conn_idle_timeout', 'id', 'ingress_traffic_pct', 'is_deprecated', 'network_scan_application', 'order_number', 'overrides_allowed', 'parent_id', 'path_affinity', 'system_app_overridden', 'transfer_type', 'use_parentapp_network_policy']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/appdefs/{}".format(api_version,
                                                                     tenant_id,
                                                                     appdef_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def appdefs_overrides(self, appdef_id, override_id, data, tenant_id=None, api_version="v2.2"):
        """
        Update a application definition overrides for system appdef

          **Parameters:**:

          - **appdef_id**: Application Definition ID
          - **override_id**: AppDef Override ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 

           - **aggregate_flows:**  Type: boolean 
           - **app_unreachability_detection:**  Type: boolean 
           - **category:**  Type: string 
           - **conn_idle_timeout:**  Type: integer 
           - **description:**  Type: string 
           - **domains:**  [Type: string] 
           - **ingress_traffic_pct:**  Type: integer 
           - **ip_rules:**           
               - **dest_filters:**  [Type: string] 
               - **dest_prefixes:**  [Type: string] 
               - **dscp:**           
                   - **value:**  Type: integer 
               - **protocol:**  Type: string 
               - **src_filters:**  [Type: string] 
           - **override_default_ip_rules:**  Type: boolean 
           - **override_default_tcp_rules:**  Type: boolean 
           - **override_default_udp_rules:**  Type: boolean 
           - **override_domains:**  Type: boolean 
           - **overrides_disable:**  Type: boolean 
           - **path_affinity:**  Type: string 
           - **session_timeout:**  Type: integer 
           - **tags:**  [Type: string] 
           - **tcp_rules:**           
               - **client_filters:**  [Type: string] 
               - **client_port:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
               - **dscp:**           
                   - **value:**  Type: integer 
               - **server_filters:**  [Type: string] 
               - **server_port:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
               - **server_prefixes:**  [Type: string] 
           - **transfer_type:**  Type: string 
           - **udp_rules:**           
               - **dest_prefixes:**  [Type: string] 
               - **dscp:**           
                   - **value:**  Type: integer 
               - **udp_filters:**  [Type: string] 
               - **udp_port:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
           - **use_parentapp_network_policy:**  Type: boolean 

          **Required Attributes:** ['aggregate_flows', 'app_unreachability_detection', 'conn_idle_timeout', 'id', 'ingress_traffic_pct', 'override_default_ip_rules', 'override_default_tcp_rules', 'override_default_udp_rules', 'override_domains', 'overrides_disable', 'session_timeout', 'use_parentapp_network_policy']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/appdefs/{}/overrides/{}".format(api_version,
                                                                                  tenant_id,
                                                                                  appdef_id,
                                                                                  override_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def appdefs_version(self, appdefs_version_id, data, tenant_id=None, api_version="v2.0"):
        """
        Change standard apps version

          **Parameters:**:

          - **appdefs_version_id**: Application Definition Version ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **app_version:**  Type: string 
           - **reqState:**  Type: string 

          **Required Attributes:** ['app_version', 'id', 'reqState']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/appdefs_version/{}".format(api_version,
                                                                             tenant_id,
                                                                             appdefs_version_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def application_probe(self, site_id, element_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update application probe configuration

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **enable_probe:**  Type: boolean 
           - **name:**  Type: string 
           - **source_interface_id:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['description', 'enable_probe', 'id', 'name', 'source_interface_id', 'tags']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/application_probe".format(api_version,
                                                                                                 tenant_id,
                                                                                                 site_id,
                                                                                                 element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def bgpconfigs(self, site_id, element_id, bgpconfig_id, data, tenant_id=None, api_version="v2.2"):
        """
        Updates BGP config

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **bgpconfig_id**: BGP Configuration ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 

           - **admin_distance:**  Type: integer 
           - **adv_interval:**  Type: integer 
           - **graceful_restart:**  Type: boolean 
           - **hold_time:**  Type: integer 
           - **keepalive_time:**  Type: integer 
           - **local_as_num:**  Type: string 
           - **maximum_paths:**  Type: integer 
           - **md5_secret:**  Type: string 
           - **multi_hop_limit:**  Type: integer 
           - **peer_auth_type:**  Type: string 
           - **peer_retry_time:**  Type: integer 
           - **prefix_adv_type:**  Type: string 
           - **prefix_adv_type_to_lan:**  Type: string 
           - **prefixes_to_adv_to_wan:**  [Type: string] 
           - **router_id:**  Type: string 
           - **stalepath_time:**  Type: integer 

          **Required Attributes:** ['admin_distance', 'graceful_restart', 'hold_time', 'id', 'keepalive_time', 'maximum_paths', 'multi_hop_limit', 'peer_auth_type', 'prefix_adv_type', 'prefix_adv_type_to_lan', 'prefixes_to_adv_to_wan', 'stalepath_time']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/bgpconfigs/{}".format(api_version,
                                                                                             tenant_id,
                                                                                             site_id,
                                                                                             element_id,
                                                                                             bgpconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def bgppeers(self, site_id, element_id, bgppeer_id, data, tenant_id=None, api_version="v2.2"):
        """
        Updates BGP Peer config

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **bgppeer_id**: BGP Peer ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 

           - **bgp_config:**           
               - **adv_interval:**  Type: integer 
               - **hold_time:**  Type: integer 
               - **keepalive_time:**  Type: integer 
               - **local_as_num:**  Type: string 
               - **md5_secret:**  Type: string 
               - **multi_hop_limit:**  Type: integer 
               - **peer_auth_type:**  Type: string 
               - **peer_retry_time:**  Type: integer 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **peer_ip:**  Type: string 
           - **peer_type:**  Type: string 
           - **remote_as_num:**  Type: string 
           - **route_map_in_id:**  Type: string 
           - **route_map_out_id:**  Type: string 
           - **scope:**  Type: string 
           - **shutdown:**  Type: boolean 
           - **tags:**  [Type: string] 
           - **update_source:**  Type: string 

          **Required Attributes:** ['bgp_config', 'id', 'peer_type', 'remote_as_num', 'route_map_in_id', 'route_map_out_id', 'scope', 'shutdown']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/bgppeers/{}".format(api_version,
                                                                                           tenant_id,
                                                                                           site_id,
                                                                                           element_id,
                                                                                           bgppeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def dhcpservers(self, site_id, dhcpserver_id, data, tenant_id=None, api_version="v2.1"):
        """
        Update an existing dhcp server configuration for a subnet

          **Parameters:**:

          - **site_id**: Site ID
          - **dhcpserver_id**: DHCP Server ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **broadcast_address:**  Type: string 
           - **custom_options:**           
               - **option_definition:**  Type: string 
               - **option_value:**  Type: string 
               - **vendor_class_identifier:**  Type: string 
           - **default_lease_time:**  Type: integer 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **dns_servers:**  [Type: string] 
           - **domain_name:**  Type: string 
           - **gateway:**  Type: string 
           - **ip_ranges:**           
               - **end_ip:**  Type: string 
               - **start_ip:**  Type: string 
           - **max_lease_time:**  Type: integer 
           - **network_context_id:**  Type: string 
           - **static_mappings:**           
               - **ip_address:**  Type: string 
               - **mac:**  Type: string 
               - **name:**  Type: string 
           - **subnet:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['broadcast_address', 'custom_options', 'default_lease_time', 'disabled', 'id', 'ip_ranges', 'max_lease_time', 'network_context_id', 'static_mappings', 'subnet']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/dhcpservers/{}".format(api_version,
                                                                                  tenant_id,
                                                                                  site_id,
                                                                                  dhcpserver_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def dnsserviceprofiles(self, dnsserviceprofile_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a DNS service profile

          **Parameters:**:

          - **dnsserviceprofile_id**: DNS Service Profile ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **authoritative_config:**           
               - **caa_records:**           
                   - **flags:**  Type: string 
                   - **name:**  Type: string 
                   - **tag:**  Type: string 
                   - **value:**  Type: string 
               - **cname_records:**           
                   - **name:**  [Type: string] 
                   - **target:**  Type: string 
                   - **ttl:**  Type: integer 
               - **dns_resource_records:**           
                   - **hex_data:**  Type: string 
                   - **name:**  Type: string 
                   - **rr_number:**  Type: integer 
               - **host_records:**           
                   - **domain_names:**  [Type: string] 
                   - **ipv4_address:**  Type: string 
                   - **ipv6_address:**  Type: string 
                   - **ttl:**  Type: integer 
               - **mx_host_records:**           
                   - **hostname:**  Type: string 
                   - **mx_name:**  Type: string 
                   - **preference:**  Type: integer 
               - **naptr_records:**           
                   - **flags:**  Type: string 
                   - **name:**  Type: string 
                   - **order:**  Type: integer 
                   - **preference:**  Type: integer 
                   - **regexp:**  Type: string 
                   - **replacement:**  Type: string 
                   - **service:**  Type: string 
               - **peers:**  [Type: string] 
               - **ptr_records:**           
                   - **name:**  Type: string 
                   - **target:**  Type: string 
               - **secondary_servers:**  [Type: string] 
               - **servers:**           
                   - **dnsservicerole_id:**  Type: string 
                   - **domain_name:**  Type: string 
               - **soa:**           
                   - **expiry:**  Type: integer 
                   - **host_master:**  Type: string 
                   - **refresh:**  Type: integer 
                   - **retry:**  Type: integer 
                   - **serial_number:**  Type: integer 
               - **srv_hosts:**           
                   - **domain_name:**  Type: string 
                   - **port:**  Type: integer 
                   - **priority:**  Type: integer 
                   - **protocol:**  Type: string 
                   - **service:**  Type: string 
                   - **target:**  Type: integer 
                   - **weight:**  Type: integer 
               - **synth_domains:**           
                   - **domain:**  Type: string 
                   - **end_ipaddress:**  Type: string 
                   - **ipaddress_prefix:**  Type: string 
                   - **prefix:**  Type: string 
                   - **start_ipaddress:**  Type: string 
               - **ttl:**  Type: integer 
               - **txt_records:**           
                   - **domain_name:**  Type: string 
                   - **texts:**  [Type: string] 
               - **zones:**           
                   - **domain_name:**  Type: string 
                   - **exclude_prefix:**  [Type: string] 
                   - **include_prefix:**  [Type: string] 
           - **cache_config:**           
               - **cache_size:**  Type: integer 
               - **disable_negative_caching:**  Type: boolean 
               - **max_cache_ttl:**  Type: integer 
               - **min_cache_ttl:**  Type: integer 
               - **negative_cache_ttl:**  Type: integer 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **dns_forward_config:**           
               - **dns_servers:**           
                   - **dnsserver_ip:**  Type: string 
                   - **dnsserver_port:**  Type: integer 
                   - **domain_names:**  [Type: string] 
                   - **forward_dnsservicerole_id:**  Type: string 
                   - **ip_prefix:**  Type: string 
                   - **source_port:**  Type: integer 
               - **max_source_port:**  Type: integer 
               - **min_source_port:**  Type: integer 
               - **send_to_all_dns_servers:**  Type: boolean 
           - **dns_queries_metadata:**           
               - **add_client_mac:**           
                   - **mac_encoding_format:**  Type: string 
               - **add_customer_premises_equipment:**           
                   - **identifier_text:**  Type: string 
                   - **type:**  Type: string 
               - **add_subnets:**           
                   - **ipv4_address:**  Type: string 
                   - **ipv4_prefix_length:**  Type: integer 
                   - **ipv6_address:**  Type: string 
                   - **ipv6_prefix_length:**  Type: integer 
           - **dns_rebind_config:**           
               - **enable_localhost_rebind:**  Type: boolean 
               - **rebind_domains:**  [Type: string] 
               - **stop_dns_rebind_privateip:**  Type: boolean 
           - **dns_response_overrides:**           
               - **aliases:**           
                   - **mask:**  Type: integer 
                   - **original_end_ip:**  Type: string 
                   - **original_ip:**  Type: string 
                   - **original_start_ip:**  Type: string 
                   - **replace_ip:**  Type: string 
               - **bogus_nx_domains:**  [Type: string] 
               - **disable_private_ip_lookups:**  Type: boolean 
               - **ignore_ip_addresses:**  [Type: string] 
               - **local_ttl:**  Type: integer 
               - **max_ttl:**  Type: integer 
           - **dnssec_config:**           
               - **disable_dnssec_timecheck:**  Type: boolean 
               - **dns_check_unsigned:**  Type: boolean 
               - **enabled:**  Type: boolean 
               - **trust_anchors:**           
                   - **anchor_class:**  Type: string 
                   - **domain:**  Type: string 
                   - **key_digest:**           
                       - **algorithm:**  Type: integer 
                       - **digest:**  Type: string 
                       - **digest_type:**  Type: integer 
                       - **key_tag:**  Type: integer 
           - **domains_to_addresses:**           
               - **domain_names:**  [Type: string] 
               - **ipv4_address:**  Type: string 
               - **ipv6_address:**  Type: string 
           - **edns_packet_max:**  Type: integer 
           - **enable_dns_loop_detection:**  Type: boolean 
           - **enable_dnssec_proxy:**  Type: boolean 
           - **enable_strict_domain_name:**  Type: boolean 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **listen_dnsservicerole_id:**  Type: string 
           - **listen_port:**  Type: integer 
           - **name:**  Type: string 
           - **region:**  Type: string 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 

          **Required Attributes:** ['authoritative_config', 'cache_config', 'disabled', 'dns_forward_config', 'dns_queries_metadata', 'dns_rebind_config', 'dns_response_overrides', 'dnssec_config', 'domains_to_addresses', 'enable_dns_loop_detection', 'enable_dnssec_proxy', 'enable_strict_domain_name', 'id', 'inactive', 'listen_port', 'region', 'tenant_id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/dnsserviceprofiles/{}".format(api_version,
                                                                                tenant_id,
                                                                                dnsserviceprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def dnsserviceroles(self, dnsservicerole_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a DNS service role

          **Parameters:**:

          - **dnsservicerole_id**: DNS Service Role ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/dnsserviceroles/{}".format(api_version,
                                                                             tenant_id,
                                                                             dnsservicerole_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def dnsservices(self, site_id, element_id, dnsservice_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a DNS service config

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **dnsservice_id**: DNS Service ID 
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **cache_config:**           
               - **cache_size:**  Type: integer 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **dns_queries_metadata:**           
               - **add_customer_premises_equipment:**           
                   - **identifier_text:**  Type: string 
                   - **type:**  Type: string 
               - **add_subnets:**           
                   - **ipv4_address:**  Type: string 
                   - **ipv4_prefix_length:**  Type: integer 
                   - **ipv6_address:**  Type: string 
                   - **ipv6_prefix_length:**  Type: integer 
           - **dnsservice_profile_id:**  Type: string 
           - **dnsservicerole_bindings:**           
               - **dnsservicerole_id:**  Type: string 
               - **interfaces:**           
                   - **admin_state_changed:**  Type: boolean 
                   - **admin_up:**  Type: boolean 
                   - **attached_lan_networks:**           
                       - **lan_network_id:**  Type: string 
                       - **vlan_id:**  Type: integer 
                   - **bound_interfaces:**           
                       - **interface_id:**  Type: string 
                       - **type:**  Type: string 
                   - **config_state:**  Type: string 
                   - **description:**  Type: string 
                   - **devicemgmt_policysetstack_id:**  Type: string 
                   - **dhcp_relay:**           
                       - **enabled:**  Type: boolean 
                       - **option_82:**           
                           - **circuit_id:**  Type: string 
                           - **enabled:**  Type: boolean 
                           - **reforwarding_policy:**  Type: string 
                           - **remote_id:**  Type: string 
                       - **server_ips:**  [Type: string] 
                       - **source_interface:**  Type: string 
                   - **directed_broadcast:**  Type: boolean 
                   - **disabled:**  Type: boolean 
                   - **disabled_reason:**  Type: string 
                   - **element_etag:**  Type: integer 
                   - **element_id:**  Type: string 
                   - **element_port_admin_up:**  Type: boolean 
                   - **ethernet_port:**           
                       - **full_duplex:**  Type: boolean 
                       - **speed:**  Type: integer 
                   - **id:**  Type: s 
                   - **ifType:**  Type: string 
                   - **inactive:**  Type: boolean 
                   - **inactive_reason:**  Type: string 
                   - **ipfixcollectorcontext_id:**  Type: string 
                   - **ipfixfiltercontext_id:**  Type: string 
                   - **ipv4_config:**           
                       - **dhcp_config:**           
                           - **client_id:**  Type: string 
                           - **hostname:**  Type: string 
                       - **dns_v4_config:**           
                           - **name_servers:**  [Type: string] 
                           - **search:**  [Type: string] 
                       - **pppoe_config:**           
                           - **chap_passwd:**  Type: string 
                           - **chap_user:**  Type: string 
                           - **set_route:**  Type: boolean 
                       - **routes:**           
                           - **destination:**  Type: string 
                           - **via:**  Type: string 
                       - **static_config:**           
                           - **address:**  Type: string 
                       - **type:**  Type: string 
                   - **ipv6_config:**           
                       - **dhcpv6:**  Type: boolean 
                       - **dns_v6_config:**           
                           - **name_servers:**  [Type: string] 
                           - **search:**  [Type: string] 
                       - **prefixes:**  [Type: string] 
                       - **type:**  Type: string 
                   - **is2kFlag:**  Type: boolean 
                   - **is_parent:**  Type: boolean 
                   - **is_service_link_parent:**  Type: boolean 
                   - **lan_state_propagation:**  Type: boolean 
                   - **mac_address:**  Type: string 
                   - **mtu:**  Type: integer 
                   - **name:**  Type: string 
                   - **nat_address:**  Type: string 
                   - **nat_pools:**           
                       - **ipv4_ranges:**           
                           - **end:**  Type: string 
                           - **start:**  Type: string 
                       - **nat_pool_id:**  Type: string 
                   - **nat_port:**  Type: integer 
                   - **nat_zone_id:**  Type: string 
                   - **network_context_id:**  Type: string 
                   - **parent:**  Type: string 
                   - **pppoe_config:**           
                       - **host_uniq:**  Type: string 
                       - **parent:**  Type: string 
                       - **password:**  Type: string 
                       - **reconnection_delay:**  Type: integer 
                       - **service_name:**  Type: string 
                       - **username:**  Type: string 
                   - **propagation_state_changed:**  Type: boolean 
                   - **region:**  Type: string 
                   - **relay_changed:**  Type: boolean 
                   - **sb_api_version:**  Type: string 
                   - **scope:**  Type: string 
                   - **secondary_ip_configs:**           
                       - **ipv4_address:**  Type: string 
                       - **scope:**  Type: string 
                   - **service_link_config:**           
                       - **gre_config:**           
                           - **csum:**  Type: boolean 
                           - **keepalive_enable:**  Type: boolean 
                           - **keepalive_fail_count:**  Type: integer 
                           - **keepalive_interval:**  Type: integer 
                       - **ipsec_config:**           
                           - **authentication:**           
                               - **certificate:**  Type: string 
                               - **ikev1_params:**           
                                   - **xauth_id:**  Type: string 
                                   - **xauth_secret:**  Type: string 
                                   - **xauth_secret_encrypted:**  Type: string 
                                   - **xauth_secret_hash:**  Type: string 
                                   - **xauth_type:**  Type: string 
                               - **local_ca_certificate:**  Type: string 
                               - **local_id:**  Type: string 
                               - **local_id_custom:**  Type: string 
                               - **passphrase:**  Type: string 
                               - **passphrase_encrypted:**  Type: string 
                               - **private_key:**  Type: string 
                               - **private_key_encrypted:**  Type: string 
                               - **remote_ca_certificate:**  Type: string 
                               - **remote_id:**  Type: string 
                               - **secret:**  Type: string 
                               - **secret_encrypted:**  Type: string 
                               - **secret_hash:**  Type: string 
                               - **type:**  Type: string 
                               - **x509Objects:**           
                                   - **certHolder:**  Type: x509certificateholder 
                                   - **certificate:**  Type: string 
                                   - **is_local_ca_cert_set:**  Type: boolean 
                                   - **is_remote_ca_cert_set:**  Type: boolean 
                                   - **keyPair:**  Type: pemkeypair 
                                   - **local_ca_certificate:**  Type: string 
                                   - **local_ca_certs_set:**  [Type: x509certificate] 
                                   - **passphrase:**  Type: string 
                                   - **private_key:**  Type: string 
                                   - **remote_ca_certificate:**  Type: string 
                                   - **remote_ca_certs_set:**  [Type: x509certificate] 
                           - **ipsec_profile_id:**  Type: string 
                       - **last_parent:**  Type: string 
                       - **parent:**  Type: string 
                       - **peer:**           
                           - **hostname:**  Type: string 
                           - **ip_addresses:**  [Type: string] 
                       - **service_endpoint_id:**  Type: string 
                       - **type:**  Type: string 
                   - **site_id:**  Type: string 
                   - **site_wan_interface_ids:**  [Type: string] 
                   - **state_id:**           
                       - **device:**  Type: string 
                       - **disabled:**  Type: boolean 
                       - **disabled_reason:**  Type: string 
                       - **dns_v4_config:**           
                           - **name_servers:**  [Type: string] 
                           - **search:**  [Type: string] 
                       - **dns_v6_config:**           
                           - **name_servers:**  [Type: string] 
                           - **search:**  [Type: string] 
                       - **element_id:**  Type: string 
                       - **extended_state:**  Type: string 
                       - **id:**  Type: s 
                       - **ike_algo:**  Type: string 
                       - **ike_last_rekeyed:**  Type: integer 
                       - **ike_next_rekey:**  Type: integer 
                       - **inactive:**  Type: boolean 
                       - **inactive_reason:**  Type: string 
                       - **index:**  Type: integer 
                       - **ipsec_algo:**  Type: string 
                       - **ipsec_last_rekeyed:**  Type: integer 
                       - **ipsec_next_rekey:**  Type: integer 
                       - **ipv4_addresses:**  [Type: string] 
                       - **ipv4_addresses_changed:**  Type: boolean 
                       - **ipv6_addresses:**  [Type: string] 
                       - **last_state_change:**  Type: integer 
                       - **local_tunnel_v4_addr:**  Type: string 
                       - **mac_address:**  Type: string 
                       - **name:**  Type: string 
                       - **negotiated_mtu:**  Type: integer 
                       - **operational_state:**  Type: string 
                       - **operational_state_changed:**  Type: boolean 
                       - **port:**           
                           - **end:**  Type: string 
                           - **start:**  Type: string 
                       - **region:**  Type: string 
                       - **remote_host_name:**  Type: string 
                       - **remote_v4_addr:**  Type: string 
                       - **routes:**           
                           - **destination:**  Type: string 
                           - **via:**  Type: string 
                       - **secondary_ipv4_addresses:**  [Type: string] 
                       - **state:**  Type: boolean 
                       - **tenant_id:**  Type: string 
                   - **static_arp_configs:**           
                       - **ipv4_address:**  Type: string 
                       - **mac_address:**  Type: string 
                   - **sub_interface:**           
                       - **vlan_id:**  Type: integer 
                   - **tags:**  [Type: string] 
                   - **tenant_id:**  Type: string 
                   - **tmpPortType:**  Type: string 
                   - **type:**  Type: string 
                   - **use_relay:**  Type: boolean 
                   - **used_for:**  Type: string 
                   - **vlan_ids:**  [Type: integer] 
                   - **wan_network_id:**  Type: string 
           - **domains_to_addresses:**           
               - **domain_names:**  [Type: string] 
               - **ipv4_address:**  Type: string 
               - **ipv6_address:**  Type: string 
           - **domains_to_interfaces:**           
               - **domain_names:**  [Type: string] 
               - **interface_id:**  Type: string 
           - **element_id:**  Type: string 
           - **enabled:**  Type: boolean 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **max_concurrent_dns_queries:**  Type: integer 
           - **name:**  Type: string 
           - **region:**  Type: string 
           - **site_id:**  Type: string 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 
           - **upperCaseName:**  Type: string 

          **Required Attributes:** ['cache_config', 'disabled', 'dns_queries_metadata', 'dnsservice_profile_id', 'dnsservicerole_bindings', 'domains_to_addresses', 'domains_to_interfaces', 'element_id', 'enabled', 'id', 'inactive', 'max_concurrent_dns_queries', 'region', 'site_id', 'tenant_id', 'upperCaseName']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/dnsservices/{}".format(api_version,
                                                                                              tenant_id,
                                                                                              site_id,
                                                                                              element_id,
                                                                                              dnsservice_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def element_admin_state(self, site_id, element_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update admin state Northbound

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **admin_action:**  Type: string 
           - **allowed_roles:**  [Type: string] 
           - **cluster_insertion_mode:**  Type: string 
           - **cluster_member_id:**  Type: string 
           - **connected:**  Type: boolean 
           - **deployment_op:**  Type: string 
           - **description:**  Type: string 
           - **hw_id:**  Type: string 
           - **model_name:**  Type: string 
           - **name:**  Type: string 
           - **role:**  Type: string 
           - **serial_number:**  Type: string 
           - **site_id:**  Type: string 
           - **software_version:**  Type: string 
           - **state:**  Type: string 

          **Required Attributes:** ['admin_action', 'allowed_roles', 'cluster_insertion_mode', 'cluster_member_id', 'connected', 'deployment_op', 'hw_id', 'id', 'model_name', 'role', 'serial_number', 'site_id', 'software_version', 'state']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/admin_state".format(api_version,
                                                                                           tenant_id,
                                                                                           site_id,
                                                                                           element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def element_extensions(self, site_id, element_id, extension_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update element level extension configuration

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **extension_id**: Extension ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **conf:**  Type: string 
           - **disabled:**  Type: boolean 
           - **name:**  Type: string 
           - **namespace:**  Type: string 

          **Required Attributes:** ['conf', 'disabled', 'id', 'namespace']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/extensions/{}".format(api_version,
                                                                                             tenant_id,
                                                                                             site_id,
                                                                                             element_id,
                                                                                             extension_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def elementaccessconfigs(self, element_id, elementaccessconfig_id, data, tenant_id=None, api_version="v2.2"):
        """
        Update an Access Config on particular element.

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **elementaccessconfig_id**: Element Access Config ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 

           - **account_disable_interval:**  Type: integer 
           - **inactive_interval:**  Type: integer 
           - **otpkey_version:**  Type: integer 
           - **retry_login_count:**  Type: integer 
           - **ssh_enabled:**  Type: boolean 
           - **ssh_outbound_enabled:**  Type: boolean 

          **Required Attributes:** ['account_disable_interval', 'id', 'inactive_interval', 'otpkey_version', 'retry_login_count', 'ssh_enabled', 'ssh_outbound_enabled']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/elementaccessconfigs/{}".format(api_version,
                                                                                              tenant_id,
                                                                                              element_id,
                                                                                              elementaccessconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def elements(self, element_id, data, tenant_id=None, api_version="v2.4"):
        """
        Used for associations and element updates

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.4)

          **Payload Attributes:** 

           - **cluster_insertion_mode:**  Type: string 
           - **cluster_member_id:**  Type: string 
           - **description:**  Type: string 
           - **l3_direct_private_wan_forwarding:**  Type: boolean 
           - **l3_lan_forwarding:**  Type: boolean 
           - **name:**  Type: string 
           - **nat_policysetstack_id:**  Type: string 
           - **network_policysetstack_id:**  Type: string 
           - **priority_policysetstack_id:**  Type: string 
           - **site_id:**  Type: string 
           - **spoke_ha_config:**           
               - **cluster_id:**  Type: string 
               - **enable:**  Type: boolean 
               - **priority:**  Type: integer 
               - **source_interface:**  Type: string 
               - **track:**           
                   - **interfaces:**           
                       - **interface_id:**  Type: string 
                       - **reduce_priority:**  Type: integer 
                   - **waninterfaces:**           
                       - **reduce_priority:**  Type: integer 
                       - **wan_interface_id:**  Type: string 
           - **sw_obj:**           
               - **location:**  Type: string 
               - **state_id:**  Type: string 
               - **version:**  Type: string 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 
           - **vpn_to_vpn_forwarding:**  Type: boolean 

          **Required Attributes:** ['cluster_insertion_mode', 'cluster_member_id', 'id', 'l3_direct_private_wan_forwarding', 'l3_lan_forwarding', 'nat_policysetstack_id', 'network_policysetstack_id', 'priority_policysetstack_id', 'site_id', 'spoke_ha_config', 'sw_obj', 'tenant_id', 'vpn_to_vpn_forwarding']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}".format(api_version,
                                                                      tenant_id,
                                                                      element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def elementsecurityzones(self, site_id, element_id, securityzone_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update an existing element security zone

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **securityzone_id**: Security Zone (ZBFW) ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **interface_ids:**  [Type: string] 
           - **lannetwork_ids:**  [Type: string] 
           - **site_id:**  Type: string 
           - **tenant_id:**  Type: string 
           - **waninterface_ids:**  [Type: string] 
           - **wanoverlay_ids:**  [Type: string] 
           - **zone_id:**  Type: string 

          **Required Attributes:** ['id', 'site_id', 'tenant_id', 'zone_id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/securityzones/{}".format(api_version,
                                                                                                tenant_id,
                                                                                                site_id,
                                                                                                element_id,
                                                                                                securityzone_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def elementusers(self, elementuser_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update an existing element user.

          **Parameters:**:

          - **elementuser_id**: Element User ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **is_tenant_level:**  Type: boolean 
           - **login_id:**  Type: string 
           - **role:**  Type: string 
           - **tenant_id:**  Type: string 
           - **username:**  Type: string 

          **Required Attributes:** ['id', 'is_tenant_level', 'login_id', 'role', 'tenant_id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elementusers/{}".format(api_version,
                                                                          tenant_id,
                                                                          elementuser_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def enterpriseprefixset(self, data, tenant_id=None, api_version="v2.0"):
        """
        PUT Enterpriseprefixset API Function

          **Parameters:**:

          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/enterpriseprefixset".format(api_version,
                                                                              tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def esp_operator_permissions_client(self, operator_id, client_id, data, tenant_id=None, api_version="v2.1"):
        """
        Create or update esp operator permissions assigned under a client

          **Parameters:**:

          - **operator_id**: Operator ID
          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **client_id:**  Type: string 
           - **custom_roles:**           
               - **custom_permissions:**           
                   - **allowed_after_ms:**  Type: integer 
                   - **allowed_before_ms:**  Type: integer 
                   - **disabled:**  Type: boolean 
                   - **disabled_reason:**  Type: string 
                   - **disallow_permission:**  Type: boolean 
                   - **id:**  Type: s 
                   - **inactive:**  Type: boolean 
                   - **inactive_reason:**  Type: string 
                   - **region:**  Type: string 
                   - **tenant_id:**  Type: string 
                   - **value:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disallow_permissions:**           
                   - **value:**  Type: string 
               - **id:**  Type: string 
               - **inactive:**  Type: boolean 
               - **name:**  Type: string 
               - **permissions:**           
                   - **value:**  Type: string 
               - **roles:**           
                   - **name:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **email:**  Type: string 
           - **enable_session_ip_lock:**  Type: boolean 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **ipv4_list:**           
               - **ipv4:**  Type: string 
           - **name:**  Type: string 
           - **operator_id:**  Type: string 
           - **region:**  Type: string 
           - **roles:**           
               - **name:**  Type: string 
           - **settings:**  Type: string 
           - **tenant_id:**  Type: string 

          **Required Attributes:** ['client_id', 'disabled', 'enable_session_ip_lock', 'id', 'inactive', 'operator_id', 'region', 'tenant_id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/operators/{}/clients/{}/permissions".format(api_version,
                                                                                              tenant_id,
                                                                                              operator_id,
                                                                                              client_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def eventcorrelationpolicyrules(self, eventcorrelationpolicyset_id, eventcorrelationpolicyrule_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update event correlation policyrule configuration

          **Parameters:**:

          - **eventcorrelationpolicyset_id**: Event Correlation Policy Set ID
          - **eventcorrelationpolicyrule_id**: Event Correlation Policy Rule ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **enabled:**  Type: boolean 
           - **end_time:**  Type: integer 
           - **escalation_rules:**           
               - **flap_rule:**           
                   - **flap_duration:**  Type: integer 
                   - **flap_rate:**  Type: integer 
               - **standing_rule:**           
                   - **priority:**  Type: string 
                   - **standing_for:**  Type: integer 
           - **event_codes:**  [Type: string] 
           - **name:**  Type: string 
           - **priority:**  Type: string 
           - **resource_ids:**  [Type: string] 
           - **resource_type:**  Type: string 
           - **start_time:**  Type: integer 
           - **sub_resource_type:**  Type: string 
           - **suppress:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['enabled', 'end_time', 'escalation_rules', 'event_codes', 'id', 'priority', 'start_time', 'suppress']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/eventcorrelationpolicysets/{}/eventcorrelationpolicyrules/{}".format(api_version,
                                                                                                                       tenant_id,
                                                                                                                       eventcorrelationpolicyset_id,
                                                                                                                       eventcorrelationpolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def eventcorrelationpolicysets(self, eventcorrelationpolicyset_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update event correlation policyset configuration

          **Parameters:**:

          - **eventcorrelationpolicyset_id**: Event Correlation Policy Set ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **active_policyset:**  Type: boolean 
           - **clone_from:**  Type: string 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyrule_order:**  [Type: string] 
           - **severity_priority_mapping:**           
               - **priority:**  Type: string 
               - **severity:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['active_policyset', 'clone_from', 'id', 'policyrule_order', 'severity_priority_mapping']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/eventcorrelationpolicysets/{}".format(api_version,
                                                                                        tenant_id,
                                                                                        eventcorrelationpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def events(self, event_id, data, tenant_id=None, api_version="v2.2"):
        """
        PUT Events API Function

          **Parameters:**:

          - **event_id**: Event ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/events/{}".format(api_version,
                                                                    tenant_id,
                                                                    event_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def externalcaconfigs(self, externalcaconfig_id, data, tenant_id=None, api_version="v2.0"):
        """
        PUT Externalcaconfigs API Function

          **Parameters:**:

          - **externalcaconfig_id**: External CA Config ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/externalcaconfigs/{}".format(api_version,
                                                                               tenant_id,
                                                                               externalcaconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def globalprefixfilters(self, globalprefixfilter_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a new global prefix filter.

          **Parameters:**:

          - **globalprefixfilter_id**: Global Prefix Filter ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **filters:**           
               - **type:**  Type: string 
           - **name:**  Type: string 

          **Required Attributes:** ['filters', 'id', 'name']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/globalprefixfilters/{}".format(api_version,
                                                                                 tenant_id,
                                                                                 globalprefixfilter_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def hubclustermembers(self, site_id, hubcluster_id, hubclustermember_id, data, tenant_id=None, api_version="v3.0"):
        """
        Update specific hub cluster member.

          **Parameters:**:

          - **site_id**: Site ID
          - **hubcluster_id**: Hub (DC) Cluster ID
          - **hubclustermember_id**: Hub Cluster Member ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/hubclusters/{}/hubclustermembers/{}".format(api_version,
                                                                                                       tenant_id,
                                                                                                       site_id,
                                                                                                       hubcluster_id,
                                                                                                       hubclustermember_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def hubclusters(self, site_id, hubcluster_id, data, tenant_id=None, api_version="v3.0"):
        """
        Update hub cluster

          **Parameters:**:

          - **site_id**: Site ID
          - **hubcluster_id**: Hub (DC) Cluster ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.0)

          **Payload Attributes:** 

           - **admin_up:**  Type: boolean 
           - **load_alarm_threshold:**  Type: integer 
           - **name:**  Type: string 
           - **subscription_factor:**  Type: number 

          **Required Attributes:** ['admin_up', 'id', 'subscription_factor']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/hubclusters/{}".format(api_version,
                                                                                  tenant_id,
                                                                                  site_id,
                                                                                  hubcluster_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def idps(self, idp_id, data, tenant_id=None, api_version="v3.2"):
        """
        Update sso

          **Parameters:**:

          - **idp_id**: SAML IDentity provider configuration ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.2)

          **Payload Attributes:** 

           - **auto_provision_operators:**  Type: boolean 
           - **auto_provision_roles:**  Type: boolean 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **idp_domain_admin_email:**  Type: string 
           - **idp_domains:**  [Type: string] 
           - **idp_entity_id:**  Type: string 
           - **idp_login_url:**  Type: string 
           - **idp_logout_url:**  Type: string 
           - **idp_metadata_b64:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **role_map:**  Type: string 
           - **session_timeout_s:**  Type: integer 
           - **sp_metadata_b64:**  Type: string 
           - **sp_x509_b64:**  Type: string 
           - **sp_x509_serial_no:**  Type: string 
           - **tenant_id:**  Type: string 

          **Required Attributes:** ['auto_provision_operators', 'auto_provision_roles', 'disabled', 'id', 'idp_domain_admin_email', 'idp_entity_id', 'idp_login_url', 'idp_logout_url', 'idp_metadata_b64', 'inactive', 'role_map', 'session_timeout_s', 'sp_metadata_b64', 'sp_x509_b64', 'sp_x509_serial_no', 'tenant_id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/idps/{}".format(api_version,
                                                                  tenant_id,
                                                                  idp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def interfaces(self, site_id, element_id, interface_id, data, tenant_id=None, api_version="v4.10"):
        """
        Provision an element interface

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **interface_id**: Interface ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v4.10)

          **Payload Attributes:** 

           - **admin_up:**  Type: boolean 
           - **attached_lan_networks:**           
               - **lan_network_id:**  Type: string 
               - **vlan_id:**  Type: integer 
           - **bound_interfaces:**  [Type: string] 
           - **bypass_pair:**           
               - **lan:**  Type: string 
               - **lan_state_propagation:**  Type: boolean 
               - **use_relay:**  Type: boolean 
               - **wan:**  Type: string 
           - **description:**  Type: string 
           - **devicemgmt_policysetstack_id:**  Type: string 
           - **dhcp_relay:**           
               - **enabled:**  Type: boolean 
               - **option_82:**           
                   - **circuit_id:**  Type: string 
                   - **enabled:**  Type: boolean 
                   - **reforwarding_policy:**  Type: string 
                   - **remote_id:**  Type: string 
               - **server_ips:**  [Type: string] 
               - **source_interface:**  Type: string 
           - **directed_broadcast:**  Type: boolean 
           - **ethernet_port:**           
               - **full_duplex:**  Type: boolean 
               - **speed:**  Type: integer 
           - **ipfixcollectorcontext_id:**  Type: string 
           - **ipfixfiltercontext_id:**  Type: string 
           - **ipv4_config:**           
               - **dhcp_config:**           
                   - **client_id:**  Type: string 
                   - **hostname:**  Type: string 
               - **dns_v4_config:**           
                   - **name_servers:**  [Type: string] 
                   - **search:**  [Type: string] 
               - **pppoe_config:**           
                   - **chap_passwd:**  Type: string 
                   - **chap_user:**  Type: string 
                   - **set_route:**  Type: boolean 
               - **routes:**           
                   - **destination:**  Type: string 
                   - **via:**  Type: string 
               - **static_config:**           
                   - **address:**  Type: string 
               - **type:**  Type: string 
           - **mac_address:**  Type: string 
           - **mtu:**  Type: integer 
           - **name:**  Type: string 
           - **nat_address:**  Type: string 
           - **nat_pools:**           
               - **ipv4_ranges:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
               - **nat_pool_id:**  Type: string 
           - **nat_port:**  Type: integer 
           - **nat_zone_id:**  Type: string 
           - **network_context_id:**  Type: string 
           - **parent:**  Type: string 
           - **pppoe_config:**           
               - **host_uniq:**  Type: string 
               - **parent:**  Type: string 
               - **password:**  Type: string 
               - **reconnection_delay:**  Type: integer 
               - **service_name:**  Type: string 
               - **username:**  Type: string 
           - **scope:**  Type: string 
           - **secondary_ip_configs:**           
               - **ipv4_address:**  Type: string 
               - **scope:**  Type: string 
           - **service_link_config:**           
               - **gre_config:**           
                   - **csum:**  Type: boolean 
                   - **keepalive_enable:**  Type: boolean 
                   - **keepalive_fail_count:**  Type: integer 
                   - **keepalive_interval:**  Type: integer 
               - **ipsec_config:**           
                   - **authentication:**           
                       - **certificate:**  Type: string 
                       - **ikev1_params:**           
                           - **xauth_id:**  Type: string 
                           - **xauth_secret:**  Type: string 
                           - **xauth_secret_encrypted:**  Type: string 
                           - **xauth_secret_hash:**  Type: string 
                           - **xauth_type:**  Type: string 
                       - **local_ca_certificate:**  Type: string 
                       - **local_id:**  Type: string 
                       - **local_id_custom:**  Type: string 
                       - **passphrase:**  Type: string 
                       - **passphrase_encrypted:**  Type: string 
                       - **private_key:**  Type: string 
                       - **private_key_encrypted:**  Type: string 
                       - **remote_ca_certificate:**  Type: string 
                       - **remote_id:**  Type: string 
                       - **secret:**  Type: string 
                       - **secret_encrypted:**  Type: string 
                       - **secret_hash:**  Type: string 
                       - **type:**  Type: string 
                       - **x509Objects:**           
                           - **certHolder:**  Type: x509certificateholder 
                           - **certificate:**  Type: string 
                           - **is_local_ca_cert_set:**  Type: boolean 
                           - **is_remote_ca_cert_set:**  Type: boolean 
                           - **keyPair:**  Type: pemkeypair 
                           - **local_ca_certificate:**  Type: string 
                           - **local_ca_certs_set:**  [Type: x509certificate] 
                           - **passphrase:**  Type: string 
                           - **private_key:**  Type: string 
                           - **remote_ca_certificate:**  Type: string 
                           - **remote_ca_certs_set:**  [Type: x509certificate] 
                   - **ipsec_profile_id:**  Type: string 
               - **last_parent:**  Type: string 
               - **parent:**  Type: string 
               - **peer:**           
                   - **hostname:**  Type: string 
                   - **ip_addresses:**  [Type: string] 
               - **service_endpoint_id:**  Type: string 
               - **type:**  Type: string 
           - **site_wan_interface_ids:**  [Type: string] 
           - **static_arp_configs:**           
               - **ipv4_address:**  Type: string 
               - **mac_address:**  Type: string 
           - **sub_interface:**           
               - **vlan_id:**  Type: integer 
           - **tags:**  [Type: string] 
           - **type:**  Type: string 
           - **used_for:**  Type: string 

          **Required Attributes:** ['admin_up', 'attached_lan_networks', 'bound_interfaces', 'bypass_pair', 'description', 'devicemgmt_policysetstack_id', 'dhcp_relay', 'directed_broadcast', 'ethernet_port', 'id', 'ipfixcollectorcontext_id', 'ipfixfiltercontext_id', 'ipv4_config', 'mac_address', 'mtu', 'name', 'nat_address', 'nat_pools', 'nat_port', 'nat_zone_id', 'network_context_id', 'parent', 'pppoe_config', 'scope', 'secondary_ip_configs', 'service_link_config', 'site_wan_interface_ids', 'static_arp_configs', 'sub_interface', 'tags', 'type', 'used_for']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/interfaces/{}".format(api_version,
                                                                                             tenant_id,
                                                                                             site_id,
                                                                                             element_id,
                                                                                             interface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ipfix(self, site_id, element_id, ipfix_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a IPFix Config

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **ipfix_id**: IPFix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **collector_config:**           
               - **host:**  Type: string 
               - **host_port:**  Type: integer 
               - **ipfixcollectorcontext_id:**  Type: string 
               - **max_message_size:**  Type: integer 
               - **protocol:**  Type: string 
           - **description:**  Type: string 
           - **export_cache_timeout:**  Type: integer 
           - **filters:**           
               - **app_def_ids:**  [Type: string] 
               - **dst_ports:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
               - **dst_prefixes_id:**  Type: string 
               - **ipfixfiltercontext_ids:**  [Type: string] 
               - **priority_traffic_types:**  [Type: string] 
               - **protocols:**  [Type: string] 
               - **rtp_transport_type:**  Type: string 
               - **src_ports:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
               - **src_prefixes_id:**  Type: string 
               - **wan_path_direction:**  Type: string 
           - **ipfixprofile_id:**  Type: string 
           - **ipfixtemplate_id:**  Type: string 
           - **name:**  Type: string 
           - **sampler:**           
               - **algorithm:**  Type: string 
               - **time_interval:**  Type: integer 
               - **time_spacing:**  Type: integer 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['collector_config', 'description', 'export_cache_timeout', 'filters', 'id', 'ipfixprofile_id', 'ipfixtemplate_id', 'name', 'sampler', 'tags']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/ipfix/{}".format(api_version,
                                                                                        tenant_id,
                                                                                        site_id,
                                                                                        element_id,
                                                                                        ipfix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ipfixcollectorcontexts(self, ipfixcollectorcontext_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a IPFix Collector context

          **Parameters:**:

          - **ipfixcollectorcontext_id**: IPFix Collector Context ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 

          **Required Attributes:** ['description', 'id', 'name']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixcollectorcontexts/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    ipfixcollectorcontext_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ipfixfiltercontexts(self, ipfixfiltercontext_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a IPFix Filter context

          **Parameters:**:

          - **ipfixfiltercontext_id**: IPFix Filter Context ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 

          **Required Attributes:** ['description', 'id', 'name']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixfiltercontexts/{}".format(api_version,
                                                                                 tenant_id,
                                                                                 ipfixfiltercontext_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ipfixglobalprefixes(self, ipfixglobalprefix_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a IPFix Global prefix

          **Parameters:**:

          - **ipfixglobalprefix_id**: IPFix Global Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['description', 'id', 'ipv4_prefixes', 'name', 'tags']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixglobalprefixes/{}".format(api_version,
                                                                                 tenant_id,
                                                                                 ipfixglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ipfixprofiles(self, ipfixprofile_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a IPFix Profile

          **Parameters:**:

          - **ipfixprofile_id**: IPFix Profile ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **collector_config:**           
               - **host:**  Type: string 
               - **host_port:**  Type: integer 
               - **ipfixcollectorcontext_id:**  Type: string 
               - **max_message_size:**  Type: integer 
               - **protocol:**  Type: string 
           - **description:**  Type: string 
           - **export_cache_timeout:**  Type: integer 
           - **filters:**           
               - **app_def_ids:**  [Type: string] 
               - **dst_ports:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
               - **dst_prefixes_id:**  Type: string 
               - **ipfixfiltercontext_ids:**  [Type: string] 
               - **priority_traffic_types:**  [Type: string] 
               - **protocols:**  [Type: string] 
               - **rtp_transport_type:**  Type: string 
               - **src_ports:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
               - **src_prefixes_id:**  Type: string 
               - **wan_path_direction:**  Type: string 
           - **ipfixtemplate_id:**  Type: string 
           - **name:**  Type: string 
           - **sampler:**           
               - **algorithm:**  Type: string 
               - **time_interval:**  Type: integer 
               - **time_spacing:**  Type: integer 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['collector_config', 'description', 'export_cache_timeout', 'filters', 'id', 'ipfixtemplate_id', 'name', 'sampler', 'tags']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixprofiles/{}".format(api_version,
                                                                           tenant_id,
                                                                           ipfixprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ipfixtemplates(self, ipfixtemplate_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a IPFix template

          **Parameters:**:

          - **ipfixtemplate_id**: IPFix Template ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **flow_fields:**  [Type: string] 
           - **generate_biflow:**  Type: boolean 
           - **name:**  Type: string 
           - **option_export_timeout:**  Type: integer 
           - **options:**  [Type: string] 
           - **tags:**  [Type: string] 
           - **template_export_timeout:**  Type: integer 

          **Required Attributes:** ['description', 'flow_fields', 'generate_biflow', 'id', 'name', 'option_export_timeout', 'options', 'tags', 'template_export_timeout']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixtemplates/{}".format(api_version,
                                                                            tenant_id,
                                                                            ipfixtemplate_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ipsecprofiles(self, ipsecprofile_id, data, tenant_id=None, api_version="v2.1"):
        """
        Update a IPSECProfile

          **Parameters:**:

          - **ipsecprofile_id**: IPSEC Profile ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **authentication:**           
               - **certificate:**  Type: string 
               - **ikev1_params:**           
                   - **xauth_id:**  Type: string 
                   - **xauth_secret:**  Type: string 
                   - **xauth_secret_encrypted:**  Type: string 
                   - **xauth_secret_hash:**  Type: string 
                   - **xauth_type:**  Type: string 
               - **local_ca_certificate:**  Type: string 
               - **local_id:**  Type: string 
               - **local_id_custom:**  Type: string 
               - **passphrase:**  Type: string 
               - **passphrase_encrypted:**  Type: string 
               - **private_key:**  Type: string 
               - **private_key_encrypted:**  Type: string 
               - **remote_ca_certificate:**  Type: string 
               - **remote_id:**  Type: string 
               - **secret:**  Type: string 
               - **secret_encrypted:**  Type: string 
               - **secret_hash:**  Type: string 
               - **type:**  Type: string 
               - **x509Objects:**           
                   - **certHolder:**  Type: x509certificateholder 
                   - **certificate:**  Type: string 
                   - **is_local_ca_cert_set:**  Type: boolean 
                   - **is_remote_ca_cert_set:**  Type: boolean 
                   - **keyPair:**  Type: pemkeypair 
                   - **local_ca_certificate:**  Type: string 
                   - **local_ca_certs_set:**  [Type: x509certificate] 
                   - **passphrase:**  Type: string 
                   - **private_key:**  Type: string 
                   - **remote_ca_certificate:**  Type: string 
                   - **remote_ca_certs_set:**  [Type: x509certificate] 
           - **description:**  Type: string 
           - **dpd_delay:**  Type: integer 
           - **dpd_enable:**  Type: boolean 
           - **dpd_timeout:**  Type: integer 
           - **esp_group:**           
               - **force_encapsulation:**  Type: boolean 
               - **lifetime:**  Type: integer 
               - **mode:**  Type: string 
               - **proposals:**           
                   - **dh_groups:**  Type: string 
                   - **encryption:**  Type: string 
                   - **hash:**  Type: string 
           - **ike_group:**           
               - **aggressive:**  Type: boolean 
               - **key_exchange:**  Type: string 
               - **lifetime:**  Type: integer 
               - **port:**  Type: integer 
               - **proposals:**           
                   - **dh_groups:**  Type: string 
                   - **encryption:**  Type: string 
                   - **hash:**  Type: string 
               - **reauth:**  Type: boolean 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['authentication', 'dpd_delay', 'dpd_enable', 'dpd_timeout', 'esp_group', 'id', 'ike_group']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipsecprofiles/{}".format(api_version,
                                                                           tenant_id,
                                                                           ipsecprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def lannetworks(self, site_id, lannetwork_id, data, tenant_id=None, api_version="v3.1"):
        """
        Update an existing LAN

          **Parameters:**:

          - **site_id**: Site ID
          - **lannetwork_id**: LAN Network ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_config:**           
               - **default_routers:**  [Type: string] 
               - **dhcp_relay:**           
                   - **enabled:**  Type: boolean 
                   - **option_82:**           
                       - **circuit_id:**  Type: string 
                       - **enabled:**  Type: boolean 
                       - **reforwarding_policy:**  Type: string 
                       - **remote_id:**  Type: string 
                   - **server_ips:**  [Type: string] 
                   - **source_interface:**  Type: string 
               - **dhcp_server:**           
                   - **domain_name:**  Type: string 
                   - **domain_name_servers:**  [Type: string] 
                   - **ip_address_pool:**           
                       - **end:**  Type: string 
                       - **start:**  Type: string 
                   - **lease_expiry_time:**  Type: integer 
                   - **lease_renew_time:**  Type: integer 
               - **prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **network_context_id:**  Type: string 
           - **scope:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['id', 'ipv4_config', 'network_context_id', 'scope']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/lannetworks/{}".format(api_version,
                                                                                  tenant_id,
                                                                                  site_id,
                                                                                  lannetwork_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def localprefixfilters(self, localprefixfilter_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a new local prefix filter.

          **Parameters:**:

          - **localprefixfilter_id**: Local Prefix Filter ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 

          **Required Attributes:** ['id', 'name']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/localprefixfilters/{}".format(api_version,
                                                                                tenant_id,
                                                                                localprefixfilter_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def natglobalprefixes(self, natglobalprefix_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update an existing NAT prefix.

          **Parameters:**:

          - **natglobalprefix_id**: NAT Global Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['id', 'ipv4_prefixes']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natglobalprefixes/{}".format(api_version,
                                                                               tenant_id,
                                                                               natglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def natlocalprefixes(self, natlocalprefix_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a  NAT local prefix.

          **Parameters:**:

          - **natlocalprefix_id**: NAT Local Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['description', 'id', 'name', 'tags']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natlocalprefixes/{}".format(api_version,
                                                                              tenant_id,
                                                                              natlocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def natpolicypools(self, natpolicypool_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a  NAT Policy Pool.

          **Parameters:**:

          - **natpolicypool_id**: NAT Policy Pool ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['description', 'id', 'name', 'tags']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicypools/{}".format(api_version,
                                                                            tenant_id,
                                                                            natpolicypool_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def natpolicyrules(self, natpolicyset_id, natpolicyrule_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update policy rule of tenant.

          **Parameters:**:

          - **natpolicyset_id**: NAT Policy Set ID
          - **natpolicyrule_id**: NAT Policy Rule ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **actions:**           
               - **nat_pool_id:**  Type: string 
               - **port:**  Type: integer 
               - **protocols:**  [Type: string] 
               - **type:**  Type: string 
           - **description:**  Type: string 
           - **destination_ports:**           
               - **from:**  Type: integer 
               - **to:**  Type: integer 
           - **destination_prefixes:**           
               - **description:**  Type: string 
               - **id:**  Type: string 
               - **ipv4_prefixes:**  [Type: string] 
               - **name:**  Type: string 
               - **tags:**  [Type: string] 
           - **destination_prefixes_id:**  Type: string 
           - **destination_zone:**           
               - **default_for_public_interfaces:**  Type: boolean 
               - **description:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **id:**  Type: s 
               - **inactive:**  Type: boolean 
               - **inactive_reason:**  Type: string 
               - **name:**  Type: string 
               - **region:**  Type: string 
               - **tags:**  [Type: string] 
               - **tenant_id:**  Type: string 
           - **destination_zone_id:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **enabled:**  Type: boolean 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **name:**  Type: string 
           - **natpolicypools:**           
               - **description:**  Type: string 
               - **id:**  Type: string 
               - **name:**  Type: string 
               - **tags:**  [Type: string] 
           - **policyset_id:**  Type: string 
           - **protocol:**  Type: integer 
           - **region:**  Type: string 
           - **source_ports:**           
               - **from:**  Type: integer 
               - **to:**  Type: integer 
           - **source_prefixes:**           
               - **description:**  Type: string 
               - **id:**  Type: string 
               - **ipv4_prefixes:**  [Type: string] 
               - **name:**  Type: string 
               - **tags:**  [Type: string] 
           - **source_prefixes_id:**  Type: string 
           - **source_zone:**           
               - **default_for_public_interfaces:**  Type: boolean 
               - **description:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **id:**  Type: s 
               - **inactive:**  Type: boolean 
               - **inactive_reason:**  Type: string 
               - **name:**  Type: string 
               - **region:**  Type: string 
               - **tags:**  [Type: string] 
               - **tenant_id:**  Type: string 
           - **source_zone_id:**  Type: string 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 

          **Required Attributes:** ['actions', 'destination_prefixes', 'destination_prefixes_id', 'destination_zone', 'destination_zone_id', 'disabled', 'enabled', 'id', 'inactive', 'natpolicypools', 'policyset_id', 'protocol', 'region', 'source_prefixes', 'source_prefixes_id', 'source_zone', 'source_zone_id', 'tenant_id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicysets/{}/natpolicyrules/{}".format(api_version,
                                                                                             tenant_id,
                                                                                             natpolicyset_id,
                                                                                             natpolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def natpolicysets(self, natpolicyset_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update NAT policy set.

          **Parameters:**:

          - **natpolicyset_id**: NAT Policy Set ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **clone_from:**  Type: string 
           - **description:**  Type: string 
           - **destination_zone_policyrule_order:**  [Type: string] 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **name:**  Type: string 
           - **policy_req_version:**  Type: string 
           - **policy_rules:**           
               - **actions:**           
                   - **nat_pool_id:**  Type: string 
                   - **port:**  Type: integer 
                   - **protocols:**  [Type: string] 
                   - **type:**  Type: string 
               - **description:**  Type: string 
               - **destination_ports:**           
                   - **from:**  Type: integer 
                   - **to:**  Type: integer 
               - **destination_prefixes:**           
                   - **description:**  Type: string 
                   - **id:**  Type: string 
                   - **ipv4_prefixes:**  [Type: string] 
                   - **name:**  Type: string 
                   - **tags:**  [Type: string] 
               - **destination_prefixes_id:**  Type: string 
               - **destination_zone:**           
                   - **default_for_public_interfaces:**  Type: boolean 
                   - **description:**  Type: string 
                   - **disabled:**  Type: boolean 
                   - **disabled_reason:**  Type: string 
                   - **id:**  Type: s 
                   - **inactive:**  Type: boolean 
                   - **inactive_reason:**  Type: string 
                   - **name:**  Type: string 
                   - **region:**  Type: string 
                   - **tags:**  [Type: string] 
                   - **tenant_id:**  Type: string 
               - **destination_zone_id:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **enabled:**  Type: boolean 
               - **id:**  Type: s 
               - **inactive:**  Type: boolean 
               - **inactive_reason:**  Type: string 
               - **name:**  Type: string 
               - **natpolicypools:**           
                   - **description:**  Type: string 
                   - **id:**  Type: string 
                   - **name:**  Type: string 
                   - **tags:**  [Type: string] 
               - **policyset_id:**  Type: string 
               - **protocol:**  Type: integer 
               - **region:**  Type: string 
               - **source_ports:**           
                   - **from:**  Type: integer 
                   - **to:**  Type: integer 
               - **source_prefixes:**           
                   - **description:**  Type: string 
                   - **id:**  Type: string 
                   - **ipv4_prefixes:**  [Type: string] 
                   - **name:**  Type: string 
                   - **tags:**  [Type: string] 
               - **source_prefixes_id:**  Type: string 
               - **source_zone:**           
                   - **default_for_public_interfaces:**  Type: boolean 
                   - **description:**  Type: string 
                   - **disabled:**  Type: boolean 
                   - **disabled_reason:**  Type: string 
                   - **id:**  Type: s 
                   - **inactive:**  Type: boolean 
                   - **inactive_reason:**  Type: string 
                   - **name:**  Type: string 
                   - **region:**  Type: string 
                   - **tags:**  [Type: string] 
                   - **tenant_id:**  Type: string 
               - **source_zone_id:**  Type: string 
               - **tags:**  [Type: string] 
               - **tenant_id:**  Type: string 
           - **region:**  Type: string 
           - **send_to_element:**  Type: boolean 
           - **source_zone_policyrule_order:**  [Type: string] 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 
           - **update_order:**  Type: boolean 

          **Required Attributes:** ['clone_from', 'disabled', 'id', 'inactive', 'policy_req_version', 'policy_rules', 'region', 'send_to_element', 'tenant_id', 'update_order']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicysets/{}".format(api_version,
                                                                           tenant_id,
                                                                           natpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def natpolicysetstacks(self, natpolicysetstack_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update NAT Policy Set Stack.

          **Parameters:**:

          - **natpolicysetstack_id**: NAT Policy Set Stack ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **default_policysetstack:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyset_ids:**  [Type: string] 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['default_policysetstack', 'id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicysetstacks/{}".format(api_version,
                                                                                tenant_id,
                                                                                natpolicysetstack_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def natzones(self, natzone_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a Nat Policy Zone.

          **Parameters:**:

          - **natzone_id**: NAT Zone ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **default_for_public_interfaces:**  Type: boolean 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **name:**  Type: string 
           - **region:**  Type: string 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 

          **Required Attributes:** ['default_for_public_interfaces', 'disabled', 'id', 'inactive', 'region', 'tenant_id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natzones/{}".format(api_version,
                                                                      tenant_id,
                                                                      natzone_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def networkcontexts(self, networkcontext_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update LAN segment

          **Parameters:**:

          - **networkcontext_id**: Network Context ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 

          **Required Attributes:** ['description', 'id', 'name']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkcontexts/{}".format(api_version,
                                                                             tenant_id,
                                                                             networkcontext_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def networkpolicyglobalprefixes(self, networkpolicyglobalprefix_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a Network global prefix.

          **Parameters:**:

          - **networkpolicyglobalprefix_id**: Network Policy Global Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['id', 'ipv4_prefixes']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicyglobalprefixes/{}".format(api_version,
                                                                                         tenant_id,
                                                                                         networkpolicyglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def networkpolicyrules(self, networkpolicyset_id, networkpolicyrule_id, data, tenant_id=None, api_version="v2.1"):
        """
        Update network policy rule of tenant.

          **Parameters:**:

          - **networkpolicyset_id**: Network Policy Set ID
          - **networkpolicyrule_id**: Network Policy Rule ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **app_def_ids:**  [Type: string] 
           - **description:**  Type: string 
           - **destination_prefixes_id:**  Type: string 
           - **enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **network_context_id:**  Type: string 
           - **order_number:**  Type: integer 
           - **paths_allowed:**           
               - **active_paths:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
               - **backup_paths:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
               - **l3_failure_paths:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
           - **service_context:**           
               - **active_service_label_id:**  Type: string 
               - **active_service_label_type:**  Type: string 
               - **backup_service_label_id:**  Type: string 
               - **backup_service_label_type:**  Type: string 
               - **type:**  Type: string 
           - **source_prefixes_id:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['app_def_ids', 'description', 'destination_prefixes_id', 'enabled', 'id', 'name', 'network_context_id', 'order_number', 'paths_allowed', 'service_context', 'source_prefixes_id', 'tags']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicysets/{}/networkpolicyrules/{}".format(api_version,
                                                                                                     tenant_id,
                                                                                                     networkpolicyset_id,
                                                                                                     networkpolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def networkpolicysets(self, networkpolicyset_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update Network Policy Set.

          **Parameters:**:

          - **networkpolicyset_id**: Network Policy Set ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicysets/{}".format(api_version,
                                                                               tenant_id,
                                                                               networkpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def networkpolicysetstacks(self, networkpolicysetstack_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a NetworkPolicySetStack

          **Parameters:**:

          - **networkpolicysetstack_id**: Network Policy Set Stack ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **default_policysetstack:**  Type: boolean 
           - **defaultrule_policyset:**           
               - **clone_from:**  Type: string 
               - **defaultrule_policyset:**  Type: boolean 
               - **description:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **id:**  Type: s 
               - **inactive:**  Type: boolean 
               - **inactive_reason:**  Type: string 
               - **name:**  Type: string 
               - **policy_req_version:**  Type: string 
               - **policy_rules:**           
                   - **app_def_ids:**  [Type: string] 
                   - **description:**  Type: string 
                   - **destination_prefixes_id:**  Type: string 
                   - **enabled:**  Type: boolean 
                   - **id:**  Type: string 
                   - **name:**  Type: string 
                   - **network_context_id:**  Type: string 
                   - **order_number:**  Type: integer 
                   - **paths_allowed:**           
                       - **active_paths:**           
                           - **label:**  Type: string 
                           - **path_type:**  Type: string 
                       - **backup_paths:**           
                           - **label:**  Type: string 
                           - **path_type:**  Type: string 
                       - **l3_failure_paths:**           
                           - **label:**  Type: string 
                           - **path_type:**  Type: string 
                   - **service_context:**           
                       - **active_service_label_id:**  Type: string 
                       - **active_service_label_type:**  Type: string 
                       - **backup_service_label_id:**  Type: string 
                       - **backup_service_label_type:**  Type: string 
                       - **type:**  Type: string 
                   - **source_prefixes_id:**  Type: string 
                   - **tags:**  [Type: string] 
               - **region:**  Type: string 
               - **send_to_element:**  Type: boolean 
               - **tags:**  [Type: string] 
               - **tenant_id:**  Type: string 
           - **defaultrule_policyset_id:**  Type: string 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **legacy_policystack:**  Type: boolean 
           - **name:**  Type: string 
           - **policyset_ids:**  [Type: string] 
           - **policysets:**           
               - **clone_from:**  Type: string 
               - **description:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **id:**  Type: s 
               - **inactive:**  Type: boolean 
               - **inactive_reason:**  Type: string 
               - **name:**  Type: string 
               - **policy_rules:**           
                   - **description:**  Type: string 
                   - **disabled:**  Type: boolean 
                   - **disabled_reason:**  Type: string 
                   - **id:**  Type: s 
                   - **inactive:**  Type: boolean 
                   - **inactive_reason:**  Type: string 
                   - **name:**  Type: string 
                   - **policyset_id:**  Type: string 
                   - **region:**  Type: string 
                   - **tags:**  [Type: string] 
                   - **tenant_id:**  Type: string 
               - **region:**  Type: string 
               - **send_to_element:**  Type: boolean 
               - **tags:**  [Type: string] 
               - **tenant_id:**  Type: string 
           - **region:**  Type: string 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 

          **Required Attributes:** ['default_policysetstack', 'defaultrule_policyset', 'defaultrule_policyset_id', 'disabled', 'id', 'inactive', 'legacy_policystack', 'policysets', 'region', 'tenant_id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicysetstacks/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    networkpolicysetstack_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ntp(self, element_id, ntp_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update an existing element NTP.

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **ntp_id**: NTP Configuration ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **ntp_servers:**           
               - **host:**  Type: string 
               - **max_poll:**  Type: integer 
               - **min_poll:**  Type: integer 
               - **version:**  Type: integer 
           - **source_interface_ids:**  [Type: string] 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['id', 'ntp_servers', 'tags']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/ntp/{}".format(api_version,
                                                                             tenant_id,
                                                                             element_id,
                                                                             ntp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def otpaccessconfigs(self, otpaccessconfig_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update an OTP Access for all elements under an Tenant.

          **Parameters:**:

          - **otpaccessconfig_id**: OTP Access configuration ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **otp_attempts:**  Type: integer 
           - **otp_validity_minutes:**  Type: integer 

          **Required Attributes:** ['id', 'otp_attempts', 'otp_validity_minutes']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/otpaccessconfigs/{}".format(api_version,
                                                                              tenant_id,
                                                                              otpaccessconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def pathgroups(self, pathgroup_id, data, tenant_id=None, api_version="v2.1"):
        """
        Update A Path Group of a tenant.

          **Parameters:**:

          - **pathgroup_id**: Path Group ID (for network service/DC routing)
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **paths:**           
               - **label:**  Type: string 
               - **path_type:**  Type: string 

          **Required Attributes:** ['description', 'id', 'name', 'paths']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/pathgroups/{}".format(api_version,
                                                                        tenant_id,
                                                                        pathgroup_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def policyrules(self, policyset_id, policyrule_id, data, tenant_id=None, api_version="v3.1"):
        """
        Update policy rule of tenant.

          **Parameters:**:

          - **policyset_id**: Policy Set ID
          - **policyrule_id**: Policy Rule ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.1)

          **Payload Attributes:** 

           - **app_def_id:**  Type: string 
           - **app_def_name:**  Type: string 
           - **default_rule:**  Type: boolean 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **lan_network_ids:**  [Type: string] 
           - **name:**  Type: string 
           - **network_context_id:**  Type: string 
           - **paths_allowed:**           
               - **active_paths:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
               - **backup_paths:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
               - **l3_failure_paths:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
           - **policy_set_id:**  Type: string 
           - **priority_num:**  Type: integer 
           - **region:**  Type: string 
           - **service_context:**           
               - **active_service_label_id:**  Type: string 
               - **active_service_label_type:**  Type: string 
               - **backup_service_label_id:**  Type: string 
               - **backup_service_label_type:**  Type: string 
               - **type:**  Type: string 
           - **site_paths_allowed:**           
               - **wn_name:**  Type: string 
               - **wp_type:**  Type: string 
           - **tenant_id:**  Type: string 

          **Required Attributes:** ['app_def_name', 'default_rule', 'disabled', 'id', 'inactive', 'lan_network_ids', 'paths_allowed', 'policy_set_id', 'priority_num', 'region', 'site_paths_allowed', 'tenant_id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/policysets/{}/policyrules/{}".format(api_version,
                                                                                       tenant_id,
                                                                                       policyset_id,
                                                                                       policyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def policysets(self, policyset_id, data, tenant_id=None, api_version="v3.0"):
        """
        Update policy set.

          **Parameters:**:

          - **policyset_id**: Policy Set ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/policysets/{}".format(api_version,
                                                                        tenant_id,
                                                                        policyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def prefixfilters(self, site_id, prefixfilter_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update an existing security prefix filter

          **Parameters:**:

          - **site_id**: Site ID
          - **prefixfilter_id**: Prefix Filter ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **filters:**           
               - **type:**  Type: string 
           - **prefix_filter_id:**  Type: string 

          **Required Attributes:** ['filters', 'id', 'prefix_filter_id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/prefixfilters/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    site_id,
                                                                                    prefixfilter_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def prioritypolicyglobalprefixes(self, prioritypolicyglobalprefix_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a  Priority global prefix.

          **Parameters:**:

          - **prioritypolicyglobalprefix_id**: Priority Policy Global Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['id', 'ipv4_prefixes']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicyglobalprefixes/{}".format(api_version,
                                                                                          tenant_id,
                                                                                          prioritypolicyglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def prioritypolicyrules(self, prioritypolicyset_id, prioritypolicyrule_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update priority policy rule of tenant.

          **Parameters:**:

          - **prioritypolicyset_id**: Priority Policy Set ID
          - **prioritypolicyrule_id**: Priority Policy Rule ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **app_def_ids:**  [Type: string] 
           - **description:**  Type: string 
           - **destination_prefixes_id:**  Type: string 
           - **dscp:**           
               - **value:**  Type: integer 
           - **enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **network_context_id:**  Type: string 
           - **order_number:**  Type: integer 
           - **priority_number:**  Type: integer 
           - **source_prefixes_id:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['destination_prefixes_id', 'dscp', 'enabled', 'id', 'network_context_id', 'order_number', 'priority_number', 'source_prefixes_id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicysets/{}/prioritypolicyrules/{}".format(api_version,
                                                                                                       tenant_id,
                                                                                                       prioritypolicyset_id,
                                                                                                       prioritypolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def prioritypolicysets(self, prioritypolicyset_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update Priority Policy Set.

          **Parameters:**:

          - **prioritypolicyset_id**: Priority Policy Set ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **bandwidth_allocation_schemes:**           
               - **bandwidth_range:**           
                   - **high:**  Type: number 
                   - **low:**  Type: number 
               - **business_priorities:**           
                   - **bandwidth_allocation:**  Type: number 
                   - **bandwidth_split_per_type:**           
                       - **bulk:**  Type: number 
                       - **rt_audio:**  Type: number 
                       - **rt_video:**  Type: number 
                       - **transactional:**  Type: number 
                   - **priority_number:**  Type: integer 
           - **business_priority_names:**           
               - **priority_name:**  Type: string 
               - **priority_num:**  Type: integer 
           - **clone_from:**  Type: string 
           - **default_rule_dscp_mappings:**           
               - **dscp:**  [Type: integer] 
               - **priority_number:**  Type: integer 
               - **transfer_type:**  Type: string 
           - **defaultrule_policyset:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 
           - **template:**  Type: boolean 

          **Required Attributes:** ['clone_from', 'defaultrule_policyset', 'id', 'template']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicysets/{}".format(api_version,
                                                                                tenant_id,
                                                                                prioritypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def prioritypolicysetstacks(self, prioritypolicysetstack_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a PriorityPolicySetStack

          **Parameters:**:

          - **prioritypolicysetstack_id**: Priority Policy Stack ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **default_policysetstack:**  Type: boolean 
           - **defaultrule_policyset_id:**  Type: string 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyset_ids:**  [Type: string] 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['default_policysetstack', 'defaultrule_policyset_id', 'id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicysetstacks/{}".format(api_version,
                                                                                     tenant_id,
                                                                                     prioritypolicysetstack_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def roles(self, role_id, data, tenant_id=None, api_version="v2.1"):
        """
        Update a custom role

          **Parameters:**:

          - **role_id**: Role ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **custom_permissions:**           
               - **allowed_after_ms:**  Type: integer 
               - **allowed_before_ms:**  Type: integer 
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **disallow_permission:**  Type: boolean 
               - **id:**  Type: s 
               - **inactive:**  Type: boolean 
               - **inactive_reason:**  Type: string 
               - **region:**  Type: string 
               - **tenant_id:**  Type: string 
               - **value:**  Type: string 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **disallow_permissions:**           
               - **value:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **is_system_owned:**  Type: boolean 
           - **name:**  Type: string 
           - **permissions:**           
               - **value:**  Type: string 
           - **region:**  Type: string 
           - **roles:**           
               - **name:**  Type: string 
           - **tenant_id:**  Type: string 

          **Required Attributes:** ['description', 'disabled', 'id', 'inactive', 'is_system_owned', 'name', 'region', 'tenant_id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/roles/{}".format(api_version,
                                                                   tenant_id,
                                                                   role_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def routing_aspathaccesslists(self, site_id, element_id, routing_aspathaccesslist_id, data, tenant_id=None, api_version="v2.1"):
        """
        Updates Access List

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_aspathaccesslist_id**: Routing AS-PATH Access List ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **as_path_regex_list:**           
               - **as_path_regex:**  Type: string 
               - **order:**  Type: integer 
               - **permit:**  Type: boolean 
           - **auto_generated:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['as_path_regex_list', 'auto_generated', 'id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_aspathaccesslists/{}".format(api_version,
                                                                                                            tenant_id,
                                                                                                            site_id,
                                                                                                            element_id,
                                                                                                            routing_aspathaccesslist_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def routing_ipcommunitylists(self, site_id, element_id, routing_ipcommunitylist_id, data, tenant_id=None, api_version="v2.0"):
        """
        Updates Community List

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_ipcommunitylist_id**: Routing IP Community List ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **auto_generated:**  Type: boolean 
           - **community_list:**           
               - **community_str:**  Type: string 
               - **permit:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['auto_generated', 'community_list', 'id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_ipcommunitylists/{}".format(api_version,
                                                                                                           tenant_id,
                                                                                                           site_id,
                                                                                                           element_id,
                                                                                                           routing_ipcommunitylist_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def routing_prefixlists(self, site_id, element_id, routing_prefixlist_id, data, tenant_id=None, api_version="v2.0"):
        """
        Updates Prefix List

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_prefixlist_id**: Routing IP Prefix List ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **auto_generated:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **prefix_filter_list:**           
               - **ge:**  Type: integer 
               - **le:**  Type: integer 
               - **order:**  Type: integer 
               - **permit:**  Type: boolean 
               - **prefix:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['auto_generated', 'id', 'prefix_filter_list']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_prefixlists/{}".format(api_version,
                                                                                                      tenant_id,
                                                                                                      site_id,
                                                                                                      element_id,
                                                                                                      routing_prefixlist_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def routing_routemaps(self, site_id, element_id, routing_routemap_id, data, tenant_id=None, api_version="v2.1"):
        """
        Updates Route Map

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_routemap_id**: Routing Route Map ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **auto_generated:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **route_map_entries:**           
               - **continue_entry:**  Type: string 
               - **match:**           
                   - **as_path_id:**  Type: string 
                   - **community_list_id:**  Type: string 
                   - **ip_next_hop_id:**  Type: string 
                   - **ip_prefix_list_id:**  Type: string 
                   - **tag:**  Type: integer 
               - **order:**  Type: integer 
               - **permit:**  Type: boolean 
               - **set:**           
                   - **as_path_prepend:**  Type: string 
                   - **community:**  Type: string 
                   - **ip_next_hop:**  Type: string 
                   - **local_preference:**  Type: integer 
                   - **tag:**  Type: integer 
                   - **weight:**  Type: integer 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['auto_generated', 'id', 'route_map_entries']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_routemaps/{}".format(api_version,
                                                                                                    tenant_id,
                                                                                                    site_id,
                                                                                                    element_id,
                                                                                                    routing_routemap_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def sdwanapps_configs(self, sdwanapp_id, config_id, data, tenant_id=None, api_version="v2.0"):
        """
        PUT Sdwanapps_Configs API Function

          **Parameters:**:

          - **sdwanapp_id**: SDWAN Application ID
          - **config_id**: SDWAN App Config ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sdwanapps/{}/configs/{}".format(api_version,
                                                                                  tenant_id,
                                                                                  sdwanapp_id,
                                                                                  config_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def securitypolicyrules(self, securitypolicyset_id, securitypolicyrule_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a tenant security policy rule.

          **Parameters:**:

          - **securitypolicyset_id**: Security Policy Set ID
          - **securitypolicyrule_id**: Security Policy Rule ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **action:**  Type: string 
           - **application_ids:**  [Type: string] 
           - **description:**  Type: string 
           - **destination_filter_ids:**  [Type: string] 
           - **destination_zone_ids:**  [Type: string] 
           - **disabled_flag:**  Type: boolean 
           - **name:**  Type: string 
           - **source_filter_ids:**  [Type: string] 
           - **source_zone_ids:**  [Type: string] 

          **Required Attributes:** ['action', 'application_ids', 'destination_filter_ids', 'destination_zone_ids', 'disabled_flag', 'id', 'source_filter_ids', 'source_zone_ids']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/securitypolicysets/{}/securitypolicyrules/{}".format(api_version,
                                                                                                       tenant_id,
                                                                                                       securitypolicyset_id,
                                                                                                       securitypolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def securitypolicysets(self, securitypolicyset_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a tenant security policy set.

          **Parameters:**:

          - **securitypolicyset_id**: Security Policy Set ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyrule_order:**  [Type: string] 

          **Required Attributes:** ['id', 'policyrule_order']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/securitypolicysets/{}".format(api_version,
                                                                                tenant_id,
                                                                                securitypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def securityzones(self, securityzone_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update an existing security zone

          **Parameters:**:

          - **securityzone_id**: Security Zone (ZBFW) ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 

          **Required Attributes:** ['id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/securityzones/{}".format(api_version,
                                                                           tenant_id,
                                                                           securityzone_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def servicebindingmaps(self, servicebindingmap_id, data, tenant_id=None, api_version="v2.1"):
        """
        Update a ServiceBindingMap

          **Parameters:**:

          - **servicebindingmap_id**: Service Binding Map ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **is_default:**  Type: boolean 
           - **name:**  Type: string 
           - **service_bindings:**           
               - **service_endpoint_ids:**  [Type: string] 
               - **service_label_id:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['id', 'is_default', 'service_bindings']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/servicebindingmaps/{}".format(api_version,
                                                                                tenant_id,
                                                                                servicebindingmap_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def serviceendpoints(self, serviceendpoint_id, data, tenant_id=None, api_version="v2.2"):
        """
        Update a ServiceEndpoint

          **Parameters:**:

          - **serviceendpoint_id**: Service Endpoint ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 

           - **address:**           
               - **city:**  Type: string 
               - **country:**  Type: string 
               - **post_code:**  Type: string 
               - **state:**  Type: string 
               - **street:**  Type: string 
               - **street2:**  Type: string 
           - **admin_up:**  Type: boolean 
           - **allow_enterprise_traffic:**  Type: boolean 
           - **description:**  Type: string 
           - **liveliness_probe:**           
               - **http:**           
                   - **failure_count:**  Type: integer 
                   - **http_status_codes:**  [Type: integer] 
                   - **interval:**  Type: integer 
                   - **url:**  Type: string 
               - **icmp_ping:**           
                   - **failure_count:**  Type: integer 
                   - **interval:**  Type: integer 
                   - **ip_addresses:**  [Type: string] 
           - **location:**           
               - **description:**  Type: string 
               - **latitude:**  Type: number 
               - **longitude:**  Type: number 
           - **name:**  Type: string 
           - **service_link_peers:**           
               - **hostnames:**  [Type: string] 
               - **ip_addresses:**  [Type: string] 
           - **site_id:**  Type: string 
           - **tags:**  [Type: string] 
           - **type:**  Type: string 

          **Required Attributes:** ['address', 'admin_up', 'allow_enterprise_traffic', 'id', 'liveliness_probe', 'location', 'service_link_peers', 'site_id', 'type']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/serviceendpoints/{}".format(api_version,
                                                                              tenant_id,
                                                                              serviceendpoint_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def servicelabels(self, servicelabel_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a ServiceLabel

          **Parameters:**:

          - **servicelabel_id**: Service Label ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 
           - **type:**  Type: string 

          **Required Attributes:** ['id', 'type']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/servicelabels/{}".format(api_version,
                                                                           tenant_id,
                                                                           servicelabel_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def site_admin_state(self, site_id, data, tenant_id=None, api_version="v3.0"):
        """
        PUT Site_Admin_State API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/admin_state".format(api_version,
                                                                               tenant_id,
                                                                               site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def site_extensions(self, site_id, extension_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update site level extension configuration

          **Parameters:**:

          - **site_id**: Site ID
          - **extension_id**: Extension ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **conf:**  Type: string 
           - **disabled:**  Type: boolean 
           - **name:**  Type: string 
           - **namespace:**  Type: string 

          **Required Attributes:** ['conf', 'disabled', 'id', 'namespace']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/extensions/{}".format(api_version,
                                                                                 tenant_id,
                                                                                 site_id,
                                                                                 extension_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def site_ipfixlocalprefixes(self, site_id, ipfixlocalprefix_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a IPFix site prefix association

          **Parameters:**:

          - **site_id**: Site ID
          - **ipfixlocalprefix_id**: IPFix Local Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['id', 'ipv4_prefixes', 'prefix_id', 'tags']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/ipfixlocalprefixes/{}".format(api_version,
                                                                                         tenant_id,
                                                                                         site_id,
                                                                                         ipfixlocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def site_natlocalprefixes(self, site_id, natlocalprefix_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update an existing Site NAT Local prefix Association

          **Parameters:**:

          - **site_id**: Site ID
          - **natlocalprefix_id**: NAT Local Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['id', 'ipv4_prefixes', 'prefix_id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/natlocalprefixes/{}".format(api_version,
                                                                                       tenant_id,
                                                                                       site_id,
                                                                                       natlocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def site_networkpolicylocalprefixes(self, site_id, networkpolicylocalprefix_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update an existing Site Network policy local prefix

          **Parameters:**:

          - **site_id**: Site ID
          - **networkpolicylocalprefix_id**: Network Policy Local Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['id', 'ipv4_prefixes', 'prefix_id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/networkpolicylocalprefixes/{}".format(api_version,
                                                                                                 tenant_id,
                                                                                                 site_id,
                                                                                                 networkpolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def site_prioritypolicylocalprefixes(self, site_id, prioritypolicylocalprefix_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update an existing Site Priority policy local prefix

          **Parameters:**:

          - **site_id**: Site ID
          - **prioritypolicylocalprefix_id**: Priority Policy Local Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['id', 'ipv4_prefixes', 'prefix_id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/prioritypolicylocalprefixes/{}".format(api_version,
                                                                                                  tenant_id,
                                                                                                  site_id,
                                                                                                  prioritypolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def siteciphers(self, site_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update site cipher

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **controller_connection_cipher:**  Type: string 
           - **site_id:**  Type: string 
           - **tenant_id:**  Type: string 
           - **vpn_ciphers:**  [Type: string] 

          **Required Attributes:** ['controller_connection_cipher', 'id', 'site_id', 'tenant_id', 'vpn_ciphers']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/siteciphers".format(api_version,
                                                                               tenant_id,
                                                                               site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def sites(self, site_id, data, tenant_id=None, api_version="v4.5"):
        """
        Update an existing site

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v4.5)

          **Payload Attributes:** 

           - **address:**           
               - **city:**  Type: string 
               - **country:**  Type: string 
               - **post_code:**  Type: string 
               - **state:**  Type: string 
               - **street:**  Type: string 
               - **street2:**  Type: string 
           - **admin_state:**  Type: string 
           - **description:**  Type: string 
           - **element_cluster_role:**  Type: string 
           - **extended_tags:**           
               - **key:**  Type: string 
               - **value:**  Type: string 
               - **value_type:**  Type: string 
           - **location:**           
               - **description:**  Type: string 
               - **latitude:**  Type: number 
               - **longitude:**  Type: number 
           - **name:**  Type: string 
           - **nat_policysetstack_id:**  Type: string 
           - **network_policysetstack_id:**  Type: string 
           - **policy_set_id:**  Type: string 
           - **priority_policysetstack_id:**  Type: string 
           - **security_policyset_id:**  Type: string 
           - **service_binding:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['address', 'admin_state', 'element_cluster_role', 'id', 'location', 'nat_policysetstack_id', 'network_policysetstack_id', 'policy_set_id', 'priority_policysetstack_id', 'security_policyset_id', 'service_binding']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}".format(api_version,
                                                                   tenant_id,
                                                                   site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def sitesecurityzones(self, site_id, sitesecurityzone_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update an existing security zone

          **Parameters:**:

          - **site_id**: Site ID
          - **sitesecurityzone_id**: Site Security Zone ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **networks:**           
               - **network_id:**  Type: string 
               - **network_type:**  Type: string 
           - **zone_id:**  Type: string 

          **Required Attributes:** ['id', 'networks', 'zone_id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/sitesecurityzones/{}".format(api_version,
                                                                                        tenant_id,
                                                                                        site_id,
                                                                                        sitesecurityzone_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def snmpagents(self, site_id, element_id, snmpagent_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update SNMP Agent

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **snmpagent_id**: SNMP Agent ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **tags:**  [Type: string] 
           - **v2_config:**           
               - **community:**  Type: string 
               - **enabled:**  Type: boolean 
           - **v3_config:**           
               - **user_access:**           
                   - **auth_phrase:**  Type: string 
                   - **auth_type:**  Type: string 
                   - **enc_phrase:**  Type: string 
                   - **enc_type:**  Type: string 
                   - **engine_id:**  Type: string 
                   - **security_level:**  Type: string 
                   - **user_name:**  Type: string 

          **Required Attributes:** ['id', 'v2_config', 'v3_config']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/snmpagents/{}".format(api_version,
                                                                                             tenant_id,
                                                                                             site_id,
                                                                                             element_id,
                                                                                             snmpagent_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def snmptraps(self, site_id, element_id, snmptrap_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update SNMP Trap

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **snmptrap_id**: SNMP Trap ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **enabled:**  Type: boolean 
           - **server_ip:**  Type: string 
           - **source_interface:**  Type: string 
           - **tags:**  [Type: string] 
           - **v2_config:**           
               - **community:**  Type: string 
               - **enabled:**  Type: boolean 
           - **v3_config:**           
               - **user_access:**           
                   - **auth_phrase:**  Type: string 
                   - **auth_type:**  Type: string 
                   - **enc_phrase:**  Type: string 
                   - **enc_type:**  Type: string 
                   - **engine_id:**  Type: string 
                   - **security_level:**  Type: string 
                   - **user_name:**  Type: string 
           - **version:**  Type: string 

          **Required Attributes:** ['enabled', 'id', 'server_ip', 'source_interface', 'v2_config', 'v3_config', 'version']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/snmptraps/{}".format(api_version,
                                                                                            tenant_id,
                                                                                            site_id,
                                                                                            element_id,
                                                                                            snmptrap_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def software(self, machine_id, software_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update Machine Software

          **Parameters:**:

          - **machine_id**: Machine ID
          - **software_id**: Software ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **scheduled_upgrade:**  Type: string 
           - **tenant_id:**  Type: string 
           - **upgrade_interval:**  Type: integer 
           - **upgrade_version:**  Type: string 

          **Required Attributes:** ['id', 'scheduled_upgrade', 'tenant_id', 'upgrade_version']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/machines/{}/software/{}".format(api_version,
                                                                                  tenant_id,
                                                                                  machine_id,
                                                                                  software_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def software_state(self, element_id, data, tenant_id=None, api_version="v2.0"):
        """
        Upgrade an element

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **download_interval:**  Type: integer 
           - **image_id:**  Type: string 
           - **interface_ids:**  [Type: string] 
           - **scheduled_download:**  Type: string 
           - **scheduled_upgrade:**  Type: string 
           - **upgrade_interval:**  Type: integer 

          **Required Attributes:** ['id', 'image_id', 'scheduled_download', 'scheduled_upgrade']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/software/state".format(api_version,
                                                                                     tenant_id,
                                                                                     element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def spokeclusters(self, site_id, spokecluster_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update Spoke Cluster

          **Parameters:**:

          - **site_id**: Site ID
          - **spokecluster_id**: Spoke Cluster ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **advertisement_interval:**  Type: number 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **preempt:**  Type: boolean 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['id', 'preempt']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/spokeclusters/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    site_id,
                                                                                    spokecluster_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def state(self, element_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update element state

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **image_id:**  Type: string 
           - **scheduled_upgrade:**  Type: string 

          **Required Attributes:** ['id', 'image_id', 'scheduled_upgrade']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/state".format(api_version,
                                                                            tenant_id,
                                                                            element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def staticroutes(self, site_id, element_id, staticroute_id, data, tenant_id=None, api_version="v2.1"):
        """
        Update static route

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **staticroute_id**: Static Route ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **destination_prefix:**  Type: string 
           - **name:**  Type: string 
           - **network_context_id:**  Type: string 
           - **nexthop_reachability_probe:**  Type: boolean 
           - **nexthops:**           
               - **admin_distance:**  Type: integer 
               - **nexthop_interface_id:**  Type: string 
               - **nexthop_ip:**  Type: string 
               - **self:**  Type: boolean 
           - **scope:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['description', 'destination_prefix', 'id', 'name', 'network_context_id', 'nexthop_reachability_probe', 'nexthops', 'scope', 'tags']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/staticroutes/{}".format(api_version,
                                                                                               tenant_id,
                                                                                               site_id,
                                                                                               element_id,
                                                                                               staticroute_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def syslogservers(self, site_id, element_id, syslogserver_id, data, tenant_id=None, api_version="v2.1"):
        """
        Update Syslog Server

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **syslogserver_id**: SYSLOG server ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **enable_flow_logging:**  Type: boolean 
           - **enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **protocol:**  Type: string 
           - **server_ip:**  Type: string 
           - **server_port:**  Type: integer 
           - **severity_level:**  Type: string 
           - **source_interface:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['description', 'enable_flow_logging', 'enabled', 'id', 'name', 'protocol', 'server_ip', 'server_port', 'severity_level', 'source_interface', 'tags']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/syslogservers/{}".format(api_version,
                                                                                                tenant_id,
                                                                                                site_id,
                                                                                                element_id,
                                                                                                syslogserver_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def templates_ntp(self, ntp_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update an existing NTP Template

          **Parameters:**:

          - **ntp_id**: NTP Configuration ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **default_template:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **ntp_servers:**           
               - **host:**  Type: string 
               - **max_poll:**  Type: integer 
               - **min_poll:**  Type: integer 
               - **version:**  Type: integer 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['default_template', 'description', 'id', 'name', 'ntp_servers', 'tags']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/templates/ntp/{}".format(api_version,
                                                                           tenant_id,
                                                                           ntp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def tenant_anynetlinks(self, anynetlink_id, data, tenant_id=None, api_version="v3.2"):
        """
        PUT Tenant_Anynetlinks API Function

          **Parameters:**:

          - **anynetlink_id**: Anynet (Secure Fabric) Link ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.2)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/anynetlinks/{}".format(api_version,
                                                                         tenant_id,
                                                                         anynetlink_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def tenant_ipfixlocalprefixes(self, ipfixlocalprefix_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a IPFix local prefix

          **Parameters:**:

          - **ipfixlocalprefix_id**: IPFix Local Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['description', 'id', 'name', 'tags']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixlocalprefixes/{}".format(api_version,
                                                                                tenant_id,
                                                                                ipfixlocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def tenant_networkpolicylocalprefixes(self, networkpolicylocalprefix_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a  Network Policy local prefix.

          **Parameters:**:

          - **networkpolicylocalprefix_id**: Network Policy Local Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['description', 'id', 'name', 'tags']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicylocalprefixes/{}".format(api_version,
                                                                                        tenant_id,
                                                                                        networkpolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def tenant_operators(self, operator_id, data, tenant_id=None, api_version="v2.1"):
        """
        Update a tenant operator

          **Parameters:**:

          - **operator_id**: Operator ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **addresses:**           
               - **city:**  Type: string 
               - **country:**  Type: string 
               - **post_code:**  Type: string 
               - **state:**  Type: string 
               - **street:**  Type: string 
               - **street2:**  Type: string 
           - **custom_roles:**           
               - **custom_permissions:**           
                   - **allowed_after_ms:**  Type: integer 
                   - **allowed_before_ms:**  Type: integer 
                   - **disabled:**  Type: boolean 
                   - **disabled_reason:**  Type: string 
                   - **disallow_permission:**  Type: boolean 
                   - **id:**  Type: s 
                   - **inactive:**  Type: boolean 
                   - **inactive_reason:**  Type: string 
                   - **region:**  Type: string 
                   - **tenant_id:**  Type: string 
                   - **value:**  Type: string 
               - **description:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **disallow_permissions:**           
                   - **value:**  Type: string 
               - **id:**  Type: string 
               - **inactive:**  Type: boolean 
               - **inactive_reason:**  Type: string 
               - **is_system_owned:**  Type: boolean 
               - **name:**  Type: string 
               - **permissions:**           
                   - **value:**  Type: string 
               - **region:**  Type: string 
               - **roles:**           
                   - **name:**  Type: string 
               - **tenant_id:**  Type: string 
           - **disable_idp_login:**  Type: boolean 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **email:**  Type: string 
           - **email_validated:**  Type: boolean 
           - **enable_session_ip_lock:**  Type: boolean 
           - **first_name:**  Type: string 
           - **from_esp:**  Type: boolean 
           - **from_esp_name:**  Type: string 
           - **from_esp_tenant_id:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **ipv4_list:**           
               - **ipv4:**  Type: string 
           - **is_locked:**  Type: boolean 
           - **is_system_owned:**  Type: boolean 
           - **last_login:**  Type: date 
           - **last_name:**  Type: string 
           - **linked_accounts:**           
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **failed_login_attempts:**  Type: integer 
               - **id:**  Type: string 
               - **inactive:**  Type: boolean 
               - **inactive_reason:**  Type: string 
               - **provider_key:**  Type: string 
               - **provider_value:**  Type: string 
               - **provider_value_updated_on:**  Type: integer 
               - **region:**  Type: string 
               - **tenant_id:**  Type: string 
           - **name:**  Type: string 
           - **phone_numbers:**           
               - **country_code:**  Type: integer 
               - **local_extension:**  Type: integer 
               - **number:**  Type: integer 
               - **types:**           
           - **region:**  Type: string 
           - **roles:**           
               - **name:**  Type: string 
           - **secondary_emails:**           
               - **email:**  Type: string 
           - **settings:**  Type: string 
           - **tenant_id:**  Type: string 

          **Required Attributes:** ['disable_idp_login', 'disabled', 'email', 'email_validated', 'enable_session_ip_lock', 'from_esp', 'from_esp_tenant_id', 'id', 'inactive', 'is_locked', 'is_system_owned', 'last_login', 'linked_accounts', 'name', 'region', 'tenant_id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/operators/{}".format(api_version,
                                                                       tenant_id,
                                                                       operator_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def tenant_permissions(self, permission_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a custom permission

          **Parameters:**:

          - **permission_id**: Permission ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **allowed_after_ms:**  Type: integer 
           - **allowed_before_ms:**  Type: integer 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **disallow_permission:**  Type: boolean 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **region:**  Type: string 
           - **tenant_id:**  Type: string 
           - **value:**  Type: string 

          **Required Attributes:** ['allowed_after_ms', 'allowed_before_ms', 'disabled', 'disallow_permission', 'id', 'inactive', 'region', 'tenant_id', 'value']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/permissions/{}".format(api_version,
                                                                         tenant_id,
                                                                         permission_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def tenant_prioritypolicylocalprefixes(self, prioritypolicylocalprefix_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a  Priority Policy local prefix.

          **Parameters:**:

          - **prioritypolicylocalprefix_id**: Priority Policy Local Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

          **Required Attributes:** ['id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicylocalprefixes/{}".format(api_version,
                                                                                         tenant_id,
                                                                                         prioritypolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def tenants(self, data, tenant_id=None, api_version="v2.1"):
        """
        Update tenant

          **Parameters:**:

          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **canonical_name:**  Type: string 
           - **clients:**  [Type: string] 
           - **is_esp:**  Type: boolean 
           - **name:**  Type: string 
           - **tenant_id:**  Type: string 

          **Required Attributes:** ['canonical_name', 'clients', 'id', 'is_esp', 'tenant_id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}".format(api_version,
                                                          tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def users(self, user_id, data, tenant_id=None, api_version="v2.0"):
        """
        PUT Users API Function

          **Parameters:**:

          - **user_id**: User ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/users/{}".format(api_version,
                                                                   tenant_id,
                                                                   user_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def vfflicense_tokens(self, vfflicense_id, token_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update Tenant Vff License Token

          **Parameters:**:

          - **vfflicense_id**: Virtual Form Factor License ID
          - **token_id**: Token ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **ion_key:**  Type: string 
           - **is_expired:**  Type: boolean 
           - **is_multiuse:**  Type: boolean 
           - **is_revoked:**  Type: boolean 
           - **is_used:**  Type: boolean 
           - **secret_key:**  Type: string 
           - **valid_till_secs:**  Type: integer 
           - **vfflicense_id:**  Type: string 

          **Required Attributes:** ['id', 'ion_key', 'is_expired', 'is_multiuse', 'is_revoked', 'is_used', 'secret_key', 'valid_till_secs', 'vfflicense_id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/vfflicenses/{}/tokens/{}".format(api_version,
                                                                                   tenant_id,
                                                                                   vfflicense_id,
                                                                                   token_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def vpnlinks_state(self, vpnlink_id, data, tenant_id=None, api_version="v2.0"):
        """
        Change the VPNLink admin state

          **Parameters:**:

          - **vpnlink_id**: VPN Link ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **al_id:**  Type: string 
           - **enabled:**  Type: boolean 

          **Required Attributes:** ['al_id', 'enabled', 'id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/vpnlinks/{}/state".format(api_version,
                                                                            tenant_id,
                                                                            vpnlink_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def waninterfacelabels(self, waninterfacelabel_id, data, tenant_id=None, api_version="v2.3"):
        """
        Update specific WAN interface label

          **Parameters:**:

          - **waninterfacelabel_id**: WAN Interface Label ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.3)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **label:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 
           - **use_for_application_reachability_probes:**  Type: boolean 
           - **use_for_controller_connections:**  Type: boolean 
           - **vpnlink_configuration:**           
               - **keep_alive_failure_count:**  Type: integer 
               - **keep_alive_interval:**  Type: integer 

          **Required Attributes:** ['description', 'id', 'label', 'name', 'tags', 'use_for_application_reachability_probes', 'use_for_controller_connections', 'vpnlink_configuration']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/waninterfacelabels/{}".format(api_version,
                                                                                tenant_id,
                                                                                waninterfacelabel_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def waninterfaces(self, site_id, waninterface_id, data, tenant_id=None, api_version="v2.6"):
        """
        Update the Site WAN interface

          **Parameters:**:

          - **site_id**: Site ID
          - **waninterface_id**: WAN Interface ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.6)

          **Payload Attributes:** 

           - **bfd_mode:**  Type: string 
           - **bw_config_mode:**  Type: string 
           - **bwc_enabled:**  Type: boolean 
           - **cost:**  Type: integer 
           - **description:**  Type: string 
           - **label_id:**  Type: string 
           - **link_bw_down:**  Type: number 
           - **link_bw_up:**  Type: number 
           - **lqm_config:**           
               - **hub_site_ids:**  [Type: string] 
               - **inter_packet_gap:**  Type: integer 
               - **statistic:**  Type: string 
           - **lqm_enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **network_id:**  Type: string 
           - **tags:**  [Type: string] 
           - **type:**  Type: string 
           - **use_for_application_reachability_probes:**  Type: boolean 
           - **use_for_controller_connections:**  Type: boolean 
           - **vpnlink_configuration:**           
               - **keep_alive_failure_count:**  Type: integer 
               - **keep_alive_interval:**  Type: integer 

          **Required Attributes:** ['bfd_mode', 'bw_config_mode', 'bwc_enabled', 'cost', 'description', 'id', 'label_id', 'link_bw_down', 'link_bw_up', 'lqm_config', 'lqm_enabled', 'name', 'network_id', 'tags', 'type', 'use_for_application_reachability_probes', 'use_for_controller_connections', 'vpnlink_configuration']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/waninterfaces/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    site_id,
                                                                                    waninterface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def wannetworks(self, wannetwork_id, data, tenant_id=None, api_version="v2.1"):
        """
        Update an existing WAN

          **Parameters:**:

          - **wannetwork_id**: WAN Network ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **provider_as_numbers:**  [Type: integer] 
           - **tags:**  [Type: string] 
           - **type:**  Type: string 

          **Required Attributes:** ['description', 'id', 'name', 'provider_as_numbers', 'tags', 'type']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/wannetworks/{}".format(api_version,
                                                                         tenant_id,
                                                                         wannetwork_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def wanoverlays(self, wanoverlay_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update app/wan context

          **Parameters:**:

          - **wanoverlay_id**: WAN Overlay ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **vni:**  Type: integer 

          **Required Attributes:** ['id']

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/wanoverlays/{}".format(api_version,
                                                                         tenant_id,
                                                                         wanoverlay_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ws_extensions(self, extension_id, data, tenant_id=None, api_version="v2.0"):
        """
        PUT Ws_Extensions API Function

          **Parameters:**:

          - **extension_id**: Extension ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ws/extensions/{}".format(api_version,
                                                                           tenant_id,
                                                                           extension_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    # Public Digest compatibility maps below, mapping what is available via
    # /v2.0/permissions API versus what is used in this SDK.

    admin_state_i = element_admin_state
    """ Backwards-compatibility alias of `admin_state_i` to `element_admin_state`"""

    admin_state_s = site_admin_state
    """ Backwards-compatibility alias of `admin_state_s` to `site_admin_state`"""

    anynetlinks_t = tenant_anynetlinks
    """ Backwards-compatibility alias of `anynetlinks_t` to `tenant_anynetlinks`"""

    configs_sdwanapps = sdwanapps_configs
    """ Backwards-compatibility alias of `configs_sdwanapps` to `sdwanapps_configs`"""

    extensions_i = element_extensions
    """ Backwards-compatibility alias of `extensions_i` to `element_extensions`"""

    extensions_s = site_extensions
    """ Backwards-compatibility alias of `extensions_s` to `site_extensions`"""

    extensions_ws = ws_extensions
    """ Backwards-compatibility alias of `extensions_ws` to `ws_extensions`"""

    ipfixlocalprefixes_s = site_ipfixlocalprefixes
    """ Backwards-compatibility alias of `ipfixlocalprefixes_s` to `site_ipfixlocalprefixes`"""

    ipfixlocalprefixes_t = tenant_ipfixlocalprefixes
    """ Backwards-compatibility alias of `ipfixlocalprefixes_t` to `tenant_ipfixlocalprefixes`"""

    natlocalprefixes_s = site_natlocalprefixes
    """ Backwards-compatibility alias of `natlocalprefixes_s` to `site_natlocalprefixes`"""

    natlocalprefixes_t = natlocalprefixes
    """ Backwards-compatibility alias of `natlocalprefixes_t` to `natlocalprefixes`"""

    networkpolicylocalprefixes_s = site_networkpolicylocalprefixes
    """ Backwards-compatibility alias of `networkpolicylocalprefixes_s` to `site_networkpolicylocalprefixes`"""

    networkpolicylocalprefixes_t = tenant_networkpolicylocalprefixes
    """ Backwards-compatibility alias of `networkpolicylocalprefixes_t` to `tenant_networkpolicylocalprefixes`"""

    ntp_templates = templates_ntp
    """ Backwards-compatibility alias of `ntp_templates` to `templates_ntp`"""

    operators_t = tenant_operators
    """ Backwards-compatibility alias of `operators_t` to `tenant_operators`"""

    overrides_appdefs = appdefs_overrides
    """ Backwards-compatibility alias of `overrides_appdefs` to `appdefs_overrides`"""

    permissions_clients_o = esp_operator_permissions_client
    """ Backwards-compatibility alias of `permissions_clients_o` to `esp_operator_permissions_client`"""

    permissions_t = tenant_permissions
    """ Backwards-compatibility alias of `permissions_t` to `tenant_permissions`"""

    prioritypolicylocalprefixes_s = site_prioritypolicylocalprefixes
    """ Backwards-compatibility alias of `prioritypolicylocalprefixes_s` to `site_prioritypolicylocalprefixes`"""

    prioritypolicylocalprefixes_t = tenant_prioritypolicylocalprefixes
    """ Backwards-compatibility alias of `prioritypolicylocalprefixes_t` to `tenant_prioritypolicylocalprefixes`"""

    state_software = software_state
    """ Backwards-compatibility alias of `state_software` to `software_state`"""

    state_vpnlinks = vpnlinks_state
    """ Backwards-compatibility alias of `state_vpnlinks` to `vpnlinks_state`"""

    tokens_vfflicenses = vfflicense_tokens
    """ Backwards-compatibility alias of `tokens_vfflicenses` to `vfflicense_tokens`"""

