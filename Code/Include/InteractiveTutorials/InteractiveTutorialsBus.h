
#pragma once

#include <AzCore/EBus/EBus.h>
#include <AzCore/Interface/Interface.h>

namespace InteractiveTutorials
{
    class InteractiveTutorialsRequests
    {
    public:
        AZ_RTTI(InteractiveTutorialsRequests, "{adf3300e-42ee-4b81-938b-100127f830b6}");
        virtual ~InteractiveTutorialsRequests() = default;
        // Put your public methods here
    };
    
    class InteractiveTutorialsBusTraits
        : public AZ::EBusTraits
    {
    public:
        //////////////////////////////////////////////////////////////////////////
        // EBusTraits overrides
        static constexpr AZ::EBusHandlerPolicy HandlerPolicy = AZ::EBusHandlerPolicy::Single;
        static constexpr AZ::EBusAddressPolicy AddressPolicy = AZ::EBusAddressPolicy::Single;
        //////////////////////////////////////////////////////////////////////////
    };

    using InteractiveTutorialsRequestBus = AZ::EBus<InteractiveTutorialsRequests, InteractiveTutorialsBusTraits>;
    using InteractiveTutorialsInterface = AZ::Interface<InteractiveTutorialsRequests>;

} // namespace InteractiveTutorials
